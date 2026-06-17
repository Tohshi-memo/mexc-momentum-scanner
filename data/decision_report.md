# Decision Report

- generated_at: 2026-06-17T13:50:54.738026+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6945**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6945, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.17%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.17% | **+0.17%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| MARKET | 20/20 | 100.0% | +0.17% | **+0.17%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.16% | **+1.16%** |
| LIMIT_BB3S_LONG | 3/6 | 50.0% | +2.14% | **+1.07%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.01% | **+0.81%** |
| ASK_LONG | 20/20 | 100.0% | +0.73% | **+0.73%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.67% | **+0.44%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 11件 (TP 5 / SL 6 / EXP 0)
- 最新: STG/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$197.02** / 初期 $100.00 (+97.02%)
- 確定: 1813件 (Win 494 / Loss 572 / Flat 747) / skip 1693件
- 成長率目線: 平均log +0.000374 / 幾何平均 +0.037% per trade / maxDD +7.25%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: COAI/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $197.02

## 4. Robust Adaptive DryRun ($100)

- 残高: **$102.06** / 初期 $100.00 (+2.06%)
- 確定: 218件 (Win 54 / Loss 50 / Flat 114) / skip 138件
- 成長率目線: 平均log +0.000093 / 幾何平均 +0.009% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0800 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AGT/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $102.06

## 5. Latest Market Context

- 更新: 2026-06-17T13:50:46.739964+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.32% price=65212.1
- Funnel: target 790 → liquid 167 → pre 50 → checked 50 → surge 4 → strict 1
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.7 >= 65=1, 4h RSI 83.1 >= 65=1, 4h RSI 66.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AGT/USDT:USDT | +88.27% | $2,933,594.54 |
| ESPORTS/USDT:USDT | +53.96% | $11,613,046.59 |
| PLAY/USDT:USDT | +27.26% | $3,231,367.90 |
| BP/USDT:USDT | +26.02% | $1,097,954.71 |
| XPL/USDT:USDT | +24.45% | $10,857,139.05 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PLAY/USDT:USDT | below_1h_threshold | +5.00% | +4.68% |
| FOLKS/USDT:USDT | below_1h_threshold | +4.75% | +4.44% |
| XPL/USDT:USDT | below_1h_threshold | +4.45% | +4.13% |
| COAI/USDT:USDT | below_1h_threshold | +2.85% | +2.53% |
| NBISSTOCK/USDT:USDT | below_1h_threshold | +2.63% | +2.32% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
