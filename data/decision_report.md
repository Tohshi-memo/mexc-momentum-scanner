# Decision Report

- generated_at: 2026-06-15T01:48:14.447481+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6721**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.87% / filled 20/20。**
- 全期間 MARKET基準: n=6721, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.87%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.87% | **+0.87%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.87% | **+0.87%** |
| ASK | 20/20 | 100.0% | +0.62% | **+0.62%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.41% | **+0.37%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 5/20 | 25.0% | +5.02% | **+1.25%** |
| LIMIT_9PCT_LONG | 7/20 | 35.0% | +2.34% | **+0.82%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.71% | **+0.60%** |
| MARKET_LONG | 20/20 | 100.0% | +0.45% | **+0.45%** |
| ASK_LONG | 20/20 | 100.0% | +0.17% | **+0.17%** |

## 2. $100 Live Portfolio

- 残高: **$100.99** / 初期 $100.00 (+0.99%)
- 確定トレード: 4件 (TP 2 / SL 2 / EXP 0)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.99
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$173.38** / 初期 $100.00 (+73.38%)
- 確定: 1594件 (Win 422 / Loss 499 / Flat 673) / skip 1688件
- 成長率目線: 平均log +0.000345 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CLO/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $173.38

## 4. Robust Adaptive DryRun ($100)

- 残高: **$99.53** / 初期 $100.00 (-0.47%)
- 確定: 90件 (Win 22 / Loss 15 / Flat 53) / skip 42件
- 成長率目線: 平均log -0.000053 / 幾何平均 -0.005% per trade / maxDD +2.07%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0708 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CLO/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $99.53

## 5. Latest Market Context

- 更新: 2026-06-15T01:48:08.548219+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=65614.9
- Funnel: target 770 → liquid 139 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 66.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| OPG/USDT:USDT | +44.18% | $7,554,976.46 |
| EVAA/USDT:USDT | +25.24% | $16,581,036.95 |
| RIF/USDT:USDT | +21.00% | $5,205,641.33 |
| H/USDT:USDT | +18.99% | $131,757,679.00 |
| CLO/USDT:USDT | +18.87% | $1,671,478.78 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CHIP/USDT:USDT | below_1h_threshold | +4.34% | +4.30% |
| AKT/USDT:USDT | below_1h_threshold | +3.21% | +3.18% |
| WLD/USDT:USDT | below_1h_threshold | +3.00% | +2.96% |
| OPG/USDT:USDT | below_1h_threshold | +2.33% | +2.29% |
| RIF/USDT:USDT | below_1h_threshold | +2.01% | +1.97% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
