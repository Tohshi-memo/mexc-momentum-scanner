# Decision Report

- generated_at: 2026-11-20T15:36:25.806476+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19248**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=19248, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |
| LIMIT_4PCT | 13/20 | 65.0% | -0.31% | **-0.20%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | -2.01% | **-0.20%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | -0.90% | **-0.45%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.28% | **+1.02%** |
| MARKET_LONG | 20/20 | 100.0% | +1.00% | **+1.00%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.06% | **+0.74%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.46% | **+0.36%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.57% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$121.25** / 初期 $100.00 (+21.25%)
- 確定トレード: 282件 (TP 102 / SL 172 / EXP 8)
- 最新: KORU/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,718.21** / 初期 $100.00 (+1618.21%)
- 確定: 7395件 (Win 2127 / Loss 2382 / Flat 2886) / skip 8414件
- 成長率目線: 平均log +0.000385 / 幾何平均 +0.038% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HUMA/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $1,718.21

## 4. Robust Adaptive DryRun ($100)

- 残高: **$440.88** / 初期 $100.00 (+340.88%)
- 確定: 5072件 (Win 1353 / Loss 1087 / Flat 2632) / skip 7587件
- 成長率目線: 平均log +0.000293 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0053 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HUMA/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $440.88

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7411件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000189 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-20T15:36:09.921378+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -2.58% price=60153.2
- Funnel: target 1087 → liquid 159 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SOXS/USDT:USDT | +33.02% | $73,199,710.06 |
| KERNEL/USDT:USDT | +31.34% | $1,455,634.28 |
| BLESS/USDT:USDT | +19.79% | $19,199,758.20 |
| HUMA/USDT:USDT | +18.84% | $1,601,285.39 |
| UVXY/USDT:USDT | +18.50% | $5,441,211.21 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MRNASTOCK/USDT:USDT | below_1h_threshold | +4.74% | +7.32% |
| GOOGLSTOCK/USDT:USDT | below_1h_threshold | +4.08% | +6.66% |
| AMZNSTOCK/USDT:USDT | below_1h_threshold | +3.05% | +5.63% |
| EVAA/USDT:USDT | below_1h_threshold | +3.01% | +5.59% |
| MSFTSTOCK/USDT:USDT | below_1h_threshold | +2.89% | +5.48% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
