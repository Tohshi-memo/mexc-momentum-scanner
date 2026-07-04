# Decision Report

- generated_at: 2026-07-04T08:13:54.888626+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8235**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8235, expectancy=-0.03%
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
| LIMIT_5PCT | 9/20 | 45.0% | -0.15% | **-0.07%** |

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

- 残高: **$314.32** / 初期 $100.00 (+214.32%)
- 確定: 2552件 (Win 798 / Loss 850 / Flat 904) / skip 2244件
- 成長率目線: 平均log +0.000449 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BEAT/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $314.32

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.63** / 初期 $100.00 (+7.63%)
- 確定: 631件 (Win 152 / Loss 152 / Flat 327) / skip 1015件
- 成長率目線: 平均log +0.000117 / 幾何平均 +0.012% per trade / maxDD +3.57%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0701 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BEAT/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $107.63

## 5. Latest Market Context

- 更新: 2026-07-04T08:13:48.904938+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=62499.9
- Funnel: target 834 → liquid 152 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ANSEM/USDT:USDT | +77.01% | $4,965,873.67 |
| TLM/USDT:USDT | +55.11% | $43,419,132.97 |
| LAB/USDT:USDT | +54.40% | $52,027,861.95 |
| HMSTR/USDT:USDT | +48.10% | $5,195,119.72 |
| VELVET/USDT:USDT | +44.03% | $30,045,825.22 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +4.75% | +4.83% |
| TAC/USDT:USDT | below_1h_threshold | +3.54% | +3.62% |
| BEAT/USDT:USDT | below_1h_threshold | +3.47% | +3.55% |
| ARPA/USDT:USDT | below_1h_threshold | +3.03% | +3.11% |
| BSB/USDT:USDT | below_1h_threshold | +2.25% | +2.33% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
