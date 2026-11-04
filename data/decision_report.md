# Decision Report

- generated_at: 2026-11-04T03:21:34.769789+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18104**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.06% / filled 20/20。**
- 全期間 MARKET基準: n=18104, expectancy=+0.03%
- 直近20件 MARKET基準: n=20, expectancy=+2.06%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.06% | **+2.06%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.06% | **+2.06%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.84% | **+1.66%** |
| LIMIT_3PCT | 12/20 | 60.0% | +1.06% | **+0.64%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.88% | **+0.62%** |
| LIMIT_BB3S | 6/18 | 33.3% | +1.21% | **+0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +4.21% | **+4.21%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +0.57% | **+0.57%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.46% | **+0.36%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.44% | **+0.20%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | -0.89% | **-0.09%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 262件 (TP 96 / SL 158 / EXP 8)
- 最新: SOXS/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,504.29** / 初期 $100.00 (+1404.29%)
- 確定: 6925件 (Win 2003 / Loss 2221 / Flat 2701) / skip 7740件
- 成長率目線: 平均log +0.000391 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SOXS/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $1,504.29

## 4. Robust Adaptive DryRun ($100)

- 残高: **$377.96** / 初期 $100.00 (+277.96%)
- 確定: 4518件 (Win 1210 / Loss 1008 / Flat 2300) / skip 6997件
- 成長率目線: 平均log +0.000294 / 幾何平均 +0.029% per trade / maxDD +4.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0427 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SOXS/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $377.96

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6265件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000139 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-04T03:21:19.330628+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.22% price=75963.7
- Funnel: target 1084 → liquid 168 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CLANKER/USDT:USDT | +34.39% | $1,497,922.43 |
| BMT/USDT:USDT | +15.12% | $1,256,833.44 |
| SOXS/USDT:USDT | +13.90% | $30,785,386.76 |
| IDOL/USDT:USDT | +9.56% | $9,740,597.49 |
| SQQQ/USDT:USDT | +7.63% | $1,228,291.28 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UNITREE/USDT:USDT | below_1h_threshold | +3.21% | +3.43% |
| SOXS/USDT:USDT | below_1h_threshold | +2.26% | +2.48% |
| APR/USDT:USDT | below_1h_threshold | +2.05% | +2.27% |
| BMT/USDT:USDT | below_1h_threshold | +1.50% | +1.72% |
| SQQQ/USDT:USDT | below_1h_threshold | +1.47% | +1.69% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
