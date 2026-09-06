# Decision Report

- generated_at: 2026-09-06T05:56:22.065878+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13801**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13801, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.53%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.53% | **-0.53%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT | 14/20 | 70.0% | +0.17% | **+0.12%** |
| LIMIT_5PCT | 2/20 | 10.0% | +0.95% | **+0.10%** |
| LIMIT_BB3S | 4/15 | 26.7% | -0.05% | **-0.01%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | -0.18% | **-0.06%** |
| MARKET | 20/20 | 100.0% | -0.53% | **-0.53%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/5 | 60.0% | +5.23% | **+3.14%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +2.21% | **+1.54%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.74% | **+1.13%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.54% | **+0.85%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +0.95% | **+0.71%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 205件 (TP 77 / SL 123 / EXP 5)
- 最新: BONER/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$860.65** / 初期 $100.00 (+760.65%)
- 確定: 5107件 (Win 1534 / Loss 1667 / Flat 1906) / skip 5255件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BASECAT/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $860.65

## 4. Robust Adaptive DryRun ($100)

- 残高: **$193.60** / 初期 $100.00 (+93.60%)
- 確定: 2546件 (Win 712 / Loss 603 / Flat 1231) / skip 4666件
- 成長率目線: 平均log +0.000259 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0169 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BASECAT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $193.60

## 5. Causal Adaptive DryRun ($100)

- 残高: **$120.12** / 初期 $100.00 (+20.12%)
- 確定: 2415件 (Win 720 / Loss 917 / Flat 778) / pending 3件 / skip 2855件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000226 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BASECAT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $120.12

## 6. Latest Market Context

- 更新: 2026-09-06T05:56:12.149885+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.16% price=79948.9
- Funnel: target 1054 → liquid 124 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ARB/USDT:USDT | +46.05% | $134,018,601.26 |
| RAY/USDT:USDT | +38.42% | $2,270,074.72 |
| FLOCK/USDT:USDT | +29.15% | $1,142,499.83 |
| UAI/USDT:USDT | +20.15% | $11,590,614.48 |
| BASECAT/USDT:USDT | +17.57% | $2,216,465.80 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PENDLE/USDT:USDT | below_1h_threshold | +4.69% | +4.54% |
| DASH/USDT:USDT | below_1h_threshold | +3.36% | +3.20% |
| FLOCK/USDT:USDT | below_1h_threshold | +2.83% | +2.67% |
| SUSHI/USDT:USDT | below_1h_threshold | +2.71% | +2.56% |
| B/USDT:USDT | below_1h_threshold | +2.66% | +2.50% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
