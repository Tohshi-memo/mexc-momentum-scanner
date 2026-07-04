# Decision Report

- generated_at: 2026-07-04T04:09:36.795461+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8216**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8216, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.83%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.83% | **-0.83%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +1.89% | **+0.57%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.40% | **+0.18%** |
| LIMIT_BB3S | 5/17 | 29.4% | +0.58% | **+0.17%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.57% | **+1.57%** |
| ASK_LONG | 20/20 | 100.0% | +1.34% | **+1.34%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +1.03% | **+0.72%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |

## 2. $100 Live Portfolio

- 残高: **$102.10** / 初期 $100.00 (+2.10%)
- 確定トレード: 57件 (TP 20 / SL 36 / EXP 1)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.10
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$302.07** / 初期 $100.00 (+202.07%)
- 確定: 2533件 (Win 785 / Loss 844 / Flat 904) / skip 2244件
- 成長率目線: 平均log +0.000436 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAB/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $302.07

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.83** / 初期 $100.00 (+5.83%)
- 確定: 612件 (Win 147 / Loss 148 / Flat 317) / skip 1015件
- 成長率目線: 平均log +0.000093 / 幾何平均 +0.009% per trade / maxDD +3.57%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0394 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ALLO/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account -0.20% 残高後 $105.83

## 5. Latest Market Context

- 更新: 2026-07-04T04:09:33.308216+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=62647.9
- Funnel: target 834 → liquid 157 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ANSEM/USDT:USDT | +83.85% | $4,129,951.79 |
| TLM/USDT:USDT | +38.28% | $39,469,920.13 |
| HMSTR/USDT:USDT | +33.21% | $2,549,404.93 |
| BAS/USDT:USDT | +31.09% | $4,133,520.41 |
| MAGMA/USDT:USDT | +28.03% | $14,885,344.19 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BASED/USDT:USDT | below_1h_threshold | +2.62% | +2.56% |
| ANSEM/USDT:USDT | below_1h_threshold | +1.88% | +1.82% |
| HMSTR/USDT:USDT | below_1h_threshold | +1.48% | +1.42% |
| BAS/USDT:USDT | below_1h_threshold | +1.24% | +1.18% |
| TLM/USDT:USDT | below_1h_threshold | +1.09% | +1.02% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
