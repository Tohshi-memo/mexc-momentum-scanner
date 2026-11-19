# Decision Report

- generated_at: 2026-11-19T01:31:20.168878+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19172**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.27% / filled 20/20。**
- 全期間 MARKET基準: n=19172, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.27%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.27% | **+1.27%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.27% | **+1.27%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.18% | **+1.12%** |
| LIMIT_2PCT | 17/20 | 85.0% | +1.15% | **+0.97%** |
| LIMIT_BB3S | 6/14 | 42.9% | +1.77% | **+0.76%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.98% | **+0.69%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/6 | 66.7% | +3.28% | **+2.19%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +4.55% | **+0.91%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +2.00% | **+0.80%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +0.83% | **+0.50%** |

## 2. $100 Live Portfolio

- 残高: **$121.25** / 初期 $100.00 (+21.25%)
- 確定トレード: 282件 (TP 102 / SL 172 / EXP 8)
- 最新: KORU/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,727.92** / 初期 $100.00 (+1627.92%)
- 確定: 7362件 (Win 2114 / Loss 2362 / Flat 2886) / skip 8371件
- 成長率目線: 平均log +0.000387 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `MARKET` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: IRYS/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $1,727.92

## 4. Robust Adaptive DryRun ($100)

- 残高: **$430.70** / 初期 $100.00 (+330.70%)
- 確定: 5021件 (Win 1335 / Loss 1087 / Flat 2599) / skip 7562件
- 成長率目線: 平均log +0.000291 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0346 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HUMA/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $430.70

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7332件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000244 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-19T01:31:07.662128+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.83% price=62639.1
- Funnel: target 1079 → liquid 142 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IRYS/USDT:USDT | +38.66% | $5,513,782.05 |
| VELVET/USDT:USDT | +24.16% | $3,913,157.64 |
| HUMA/USDT:USDT | +14.89% | $2,405,243.59 |
| PHAROS/USDT:USDT | +14.25% | $1,929,330.62 |
| LUNC/USDT:USDT | +13.14% | $1,703,426.34 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CSOPSKHYNIX2L/USDT:USDT | below_1h_threshold | +4.39% | +5.22% |
| KORU/USDT:USDT | below_1h_threshold | +3.99% | +4.81% |
| BLESS/USDT:USDT | below_1h_threshold | +3.50% | +4.33% |
| SOXL/USDT:USDT | below_1h_threshold | +2.63% | +3.46% |
| SNXX/USDT:USDT | below_1h_threshold | +2.17% | +2.99% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
