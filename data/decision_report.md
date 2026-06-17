# Decision Report

- generated_at: 2026-06-17T13:36:51.763647+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6944**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6944, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.17%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.17% | **+0.17%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| ASK | 20/20 | 100.0% | +0.17% | **+0.17%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/6 | 50.0% | +2.14% | **+1.07%** |
| MARKET_LONG | 20/20 | 100.0% | +0.76% | **+0.76%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.03% | **+0.51%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.46% | **+0.36%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.44% | **+0.35%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 11件 (TP 5 / SL 6 / EXP 0)
- 最新: STG/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$197.02** / 初期 $100.00 (+97.02%)
- 確定: 1813件 (Win 494 / Loss 572 / Flat 747) / skip 1692件
- 成長率目線: 平均log +0.000374 / 幾何平均 +0.037% per trade / maxDD +7.25%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: COAI/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $197.02

## 4. Robust Adaptive DryRun ($100)

- 残高: **$101.62** / 初期 $100.00 (+1.62%)
- 確定: 217件 (Win 53 / Loss 50 / Flat 114) / skip 138件
- 成長率目線: 平均log +0.000074 / 幾何平均 +0.007% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0851 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: STG/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $101.62

## 5. Latest Market Context

- 更新: 2026-06-17T13:36:44.047797+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=65042.2
- Funnel: target 790 → liquid 167 → pre 50 → checked 50 → surge 4 → strict 1
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.7 >= 65=1, 4h RSI 77.0 >= 65=1, 4h RSI 81.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AGT/USDT:USDT | +79.22% | $2,485,992.35 |
| ESPORTS/USDT:USDT | +60.08% | $11,401,864.77 |
| XPL/USDT:USDT | +27.91% | $9,963,552.50 |
| BP/USDT:USDT | +27.64% | $1,083,718.89 |
| PLAY/USDT:USDT | +26.50% | $3,105,615.89 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PLAY/USDT:USDT | below_1h_threshold | +4.37% | +4.32% |
| WDCSTOCK/USDT:USDT | below_1h_threshold | +3.68% | +3.63% |
| BP/USDT:USDT | below_1h_threshold | +2.28% | +2.23% |
| COAI/USDT:USDT | below_1h_threshold | +2.20% | +2.15% |
| FOLKS/USDT:USDT | below_1h_threshold | +1.92% | +1.86% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
