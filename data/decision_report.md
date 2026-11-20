# Decision Report

- generated_at: 2026-11-20T16:26:36.840852+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19253**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.00% / filled 20/20。**
- 全期間 MARKET基準: n=19253, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+2.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.00% | **+2.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.00% | **+2.00%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.22% | **+0.92%** |
| LIMIT_1PCT | 15/20 | 75.0% | +0.48% | **+0.36%** |
| LIMIT_3PCT | 12/20 | 60.0% | +0.27% | **+0.16%** |
| LIMIT_5PCT | 3/20 | 15.0% | +0.95% | **+0.14%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +2.00% | **+1.00%** |
| LIMIT_9PCT_LONG | 7/20 | 35.0% | +2.34% | **+0.82%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +0.45% | **+0.22%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | -0.10% | **-0.08%** |

## 2. $100 Live Portfolio

- 残高: **$121.25** / 初期 $100.00 (+21.25%)
- 確定トレード: 282件 (TP 102 / SL 172 / EXP 8)
- 最新: KORU/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,692.53** / 初期 $100.00 (+1592.53%)
- 確定: 7400件 (Win 2128 / Loss 2386 / Flat 2886) / skip 8414件
- 成長率目線: 平均log +0.000382 / 幾何平均 +0.038% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $1,692.53

## 4. Robust Adaptive DryRun ($100)

- 残高: **$440.88** / 初期 $100.00 (+340.88%)
- 確定: 5077件 (Win 1353 / Loss 1087 / Flat 2637) / skip 7587件
- 成長率目線: 平均log +0.000292 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0096 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $440.88

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7418件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000113 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-20T16:26:18.815163+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.32% price=59255.0
- Funnel: target 1087 → liquid 162 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.6 >= 65=1, 4h RSI 75.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +14.68% | $22,750,559.58 |
| HUMA/USDT:USDT | +3.17% | $1,686,277.11 |
| JCT/USDT:USDT | +2.10% | $3,013,878.77 |
| NIGHT/USDT:USDT | +2.06% | $1,024,305.98 |
| SOXS/USDT:USDT | +2.02% | $71,803,426.01 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HUMA/USDT:USDT | below_1h_threshold | +3.18% | +3.50% |
| JCT/USDT:USDT | below_1h_threshold | +2.17% | +2.49% |
| NIGHT/USDT:USDT | below_1h_threshold | +2.07% | +2.39% |
| MMT/USDT:USDT | below_1h_threshold | +1.52% | +1.84% |
| PIEVERSE/USDT:USDT | below_1h_threshold | +1.46% | +1.78% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
