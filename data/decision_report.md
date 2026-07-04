# Decision Report

- generated_at: 2026-07-04T07:34:44.935488+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8232**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8232, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=-2.50%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.50% | **-2.50%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 9/20 | 45.0% | +1.23% | **+0.55%** |
| LIMIT_7PCT | 6/20 | 30.0% | +1.67% | **+0.50%** |
| LIMIT_8PCT | 4/20 | 20.0% | +1.78% | **+0.36%** |
| LIMIT_5PCT | 12/20 | 60.0% | +0.13% | **+0.08%** |
| LIMIT_9PCT | 2/20 | 10.0% | +0.29% | **+0.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +2.31% | **+2.31%** |
| MARKET_LONG | 20/20 | 100.0% | +1.92% | **+1.92%** |
| LIMIT_3PCT_LONG | 8/20 | 40.0% | +4.23% | **+1.69%** |
| LIMIT_2PCT_LONG | 10/20 | 50.0% | +3.38% | **+1.69%** |
| LIMIT_1PCT_LONG | 13/20 | 65.0% | +2.60% | **+1.69%** |

## 2. $100 Live Portfolio

- 残高: **$102.10** / 初期 $100.00 (+2.10%)
- 確定トレード: 57件 (TP 20 / SL 36 / EXP 1)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.10
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$312.76** / 初期 $100.00 (+212.76%)
- 確定: 2549件 (Win 796 / Loss 849 / Flat 904) / skip 2244件
- 成長率目線: 平均log +0.000447 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $312.76

## 4. Robust Adaptive DryRun ($100)

- 残高: **$108.01** / 初期 $100.00 (+8.01%)
- 確定: 628件 (Win 152 / Loss 151 / Flat 325) / skip 1015件
- 成長率目線: 平均log +0.000123 / 幾何平均 +0.012% per trade / maxDD +3.57%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1006 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.52% 残高後 $108.01

## 5. Latest Market Context

- 更新: 2026-07-04T07:34:38.760236+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=62507.9
- Funnel: target 834 → liquid 153 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ANSEM/USDT:USDT | +78.71% | $4,867,971.05 |
| VELVET/USDT:USDT | +53.35% | $28,325,157.37 |
| TLM/USDT:USDT | +52.55% | $43,104,653.48 |
| HMSTR/USDT:USDT | +48.36% | $4,758,278.21 |
| LAB/USDT:USDT | +42.19% | $50,645,362.30 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSB/USDT:USDT | below_1h_threshold | +3.91% | +3.85% |
| GPS/USDT:USDT | below_1h_threshold | +3.29% | +3.23% |
| ANSEM/USDT:USDT | below_1h_threshold | +3.11% | +3.06% |
| NEX/USDT:USDT | below_1h_threshold | +1.66% | +1.61% |
| BAS/USDT:USDT | below_1h_threshold | +1.55% | +1.50% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
