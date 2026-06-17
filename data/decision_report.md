# Decision Report

- generated_at: 2026-06-17T13:58:04.749488+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6946**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6946, expectancy=-0.05%
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
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| MARKET | 20/20 | 100.0% | +0.17% | **+0.17%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.16% | **+1.16%** |
| LIMIT_BB3S_LONG | 3/6 | 50.0% | +2.14% | **+1.07%** |
| ASK_LONG | 20/20 | 100.0% | +0.75% | **+0.75%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +0.74% | **+0.55%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.67% | **+0.44%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 11件 (TP 5 / SL 6 / EXP 0)
- 最新: STG/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$197.02** / 初期 $100.00 (+97.02%)
- 確定: 1813件 (Win 494 / Loss 572 / Flat 747) / skip 1694件
- 成長率目線: 平均log +0.000374 / 幾何平均 +0.037% per trade / maxDD +7.25%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: COAI/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $197.02

## 4. Robust Adaptive DryRun ($100)

- 残高: **$102.06** / 初期 $100.00 (+2.06%)
- 確定: 219件 (Win 54 / Loss 50 / Flat 115) / skip 138件
- 成長率目線: 平均log +0.000093 / 幾何平均 +0.009% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0704 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BR/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $102.06

## 5. Latest Market Context

- 更新: 2026-06-17T13:57:55.940768+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.39% price=65256.9
- Funnel: target 790 → liquid 167 → pre 50 → checked 50 → surge 5 → strict 1
- Surge前reject: below_1h_threshold=45, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.2 >= 65=1, 4h RSI 68.4 >= 65=1, 4h RSI 83.5 >= 65=1, 4h RSI 66.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AGT/USDT:USDT | +90.07% | $3,255,460.66 |
| ESPORTS/USDT:USDT | +56.08% | $11,677,559.28 |
| BP/USDT:USDT | +26.30% | $1,100,018.83 |
| PLAY/USDT:USDT | +26.09% | $3,277,038.30 |
| BLESS/USDT:USDT | +22.78% | $16,978,726.96 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PLAY/USDT:USDT | below_1h_threshold | +4.04% | +3.65% |
| XPL/USDT:USDT | below_1h_threshold | +3.51% | +3.13% |
| COAI/USDT:USDT | below_1h_threshold | +2.88% | +2.49% |
| FOXASTOCK/USDT:USDT | below_1h_threshold | +2.62% | +2.24% |
| BLESS/USDT:USDT | below_1h_threshold | +2.00% | +1.62% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
