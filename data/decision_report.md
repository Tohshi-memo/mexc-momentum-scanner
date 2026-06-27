# Decision Report

- generated_at: 2026-06-27T23:43:29.002290+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7718**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7718, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.76%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.76% | **-0.76%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 4/20 | 20.0% | +5.46% | **+1.09%** |
| LIMIT_10PCT | 3/20 | 15.0% | -0.85% | **-0.13%** |
| LIMIT_9PCT | 3/20 | 15.0% | -1.14% | **-0.17%** |
| LIMIT_5PCT | 6/20 | 30.0% | -1.52% | **-0.45%** |
| LIMIT_7PCT | 4/20 | 20.0% | -2.29% | **-0.46%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.96% | **+1.96%** |
| ASK_LONG | 20/20 | 100.0% | +1.88% | **+1.88%** |
| LIMIT_1PCT_LONG | 12/20 | 60.0% | +1.15% | **+0.69%** |
| LIMIT_2PCT_LONG | 10/20 | 50.0% | +0.98% | **+0.49%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +0.74% | **+0.37%** |

## 2. $100 Live Portfolio

- 残高: **$102.65** / 初期 $100.00 (+2.65%)
- 確定トレード: 41件 (TP 15 / SL 25 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.65
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$239.54** / 初期 $100.00 (+139.54%)
- 確定: 2227件 (Win 669 / Loss 743 / Flat 815) / skip 2052件
- 成長率目線: 平均log +0.000392 / 幾何平均 +0.039% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `MARKET_LONG` TP_HIT account +1.00% 残高後 $239.54

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.96** / 初期 $100.00 (+7.96%)
- 確定: 449件 (Win 120 / Loss 115 / Flat 214) / skip 680件
- 成長率目線: 平均log +0.000171 / 幾何平均 +0.017% per trade / maxDD +3.03%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0484 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $107.96

## 5. Latest Market Context

- 更新: 2026-06-27T23:43:24.198351+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.25% price=60055.1
- Funnel: target 806 → liquid 122 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 89.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +13.57% | $242,165,790.85 |
| BAS/USDT:USDT | +11.81% | $2,481,268.31 |
| RE/USDT:USDT | +10.20% | $7,040,516.48 |
| SLX/USDT:USDT | +8.60% | $18,957,320.97 |
| S/USDT:USDT | +7.88% | $4,442,970.31 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BAS/USDT:USDT | below_1h_threshold | +2.73% | +2.98% |
| RE/USDT:USDT | below_1h_threshold | +2.36% | +2.61% |
| BASED/USDT:USDT | below_1h_threshold | +1.98% | +2.23% |
| ARX/USDT:USDT | below_1h_threshold | +1.91% | +2.16% |
| MYX/USDT:USDT | below_1h_threshold | +1.57% | +1.82% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
