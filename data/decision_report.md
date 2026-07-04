# Decision Report

- generated_at: 2026-07-04T07:54:45.919828+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8234**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8234, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=-1.90%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.90% | **-1.90%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 7/20 | 35.0% | +1.05% | **+0.37%** |
| LIMIT_7PCT | 5/20 | 25.0% | +1.44% | **+0.36%** |
| LIMIT_8PCT | 3/20 | 15.0% | +1.14% | **+0.17%** |
| LIMIT_9PCT | 2/20 | 10.0% | +0.29% | **+0.03%** |
| LIMIT_5PCT | 10/20 | 50.0% | -0.04% | **-0.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.90% | **+1.90%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +3.31% | **+1.49%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +3.26% | **+1.46%** |
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +2.00% | **+1.33%** |
| MARKET_LONG | 20/20 | 100.0% | +1.32% | **+1.32%** |

## 2. $100 Live Portfolio

- 残高: **$102.10** / 初期 $100.00 (+2.10%)
- 確定トレード: 57件 (TP 20 / SL 36 / EXP 1)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.10
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$312.75** / 初期 $100.00 (+212.75%)
- 確定: 2551件 (Win 797 / Loss 850 / Flat 904) / skip 2244件
- 成長率目線: 平均log +0.000447 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $312.75

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.63** / 初期 $100.00 (+7.63%)
- 確定: 630件 (Win 152 / Loss 152 / Flat 326) / skip 1015件
- 成長率目線: 平均log +0.000117 / 幾何平均 +0.012% per trade / maxDD +3.57%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0815 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $107.63

## 5. Latest Market Context

- 更新: 2026-07-04T07:54:38.816364+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.13% price=62556.6
- Funnel: target 834 → liquid 154 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ANSEM/USDT:USDT | +80.15% | $4,914,529.70 |
| TLM/USDT:USDT | +61.95% | $43,687,699.00 |
| HMSTR/USDT:USDT | +50.08% | $4,980,505.08 |
| VELVET/USDT:USDT | +43.98% | $30,194,655.71 |
| LAB/USDT:USDT | +42.91% | $51,509,102.37 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VELVET/USDT:USDT | below_1h_threshold | +4.67% | +4.54% |
| BSB/USDT:USDT | below_1h_threshold | +4.60% | +4.47% |
| ANSEM/USDT:USDT | below_1h_threshold | +3.95% | +3.81% |
| NEX/USDT:USDT | below_1h_threshold | +3.77% | +3.63% |
| GPS/USDT:USDT | below_1h_threshold | +3.02% | +2.88% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
