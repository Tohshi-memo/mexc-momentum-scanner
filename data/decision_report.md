# Decision Report

- generated_at: 2026-10-24T03:31:14.874121+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17329**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.59% / filled 20/20。**
- 全期間 MARKET基準: n=17329, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.59%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.59% | **+0.59%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 6/20 | 30.0% | +5.13% | **+1.54%** |
| LIMIT_6PCT | 6/20 | 30.0% | +4.00% | **+1.20%** |
| LIMIT_8PCT | 5/20 | 25.0% | +4.74% | **+1.19%** |
| LIMIT_5PCT | 8/20 | 40.0% | +2.62% | **+1.05%** |
| LIMIT_9PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/6 | 33.3% | +7.02% | **+2.34%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +2.85% | **+0.85%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +1.78% | **+0.80%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +1.30% | **+0.58%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 250件 (TP 92 / SL 150 / EXP 8)
- 最新: MSTRSTOCK/USDT:USDT EXPIRED PnL +0.27% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,323.53** / 初期 $100.00 (+1223.53%)
- 確定: 6582件 (Win 1906 / Loss 2100 / Flat 2576) / skip 7308件
- 成長率目線: 平均log +0.000392 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BMT/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $1,323.53

## 4. Robust Adaptive DryRun ($100)

- 残高: **$298.55** / 初期 $100.00 (+198.55%)
- 確定: 3929件 (Win 1083 / Loss 920 / Flat 1926) / skip 6811件
- 成長率目線: 平均log +0.000278 / 幾何平均 +0.028% per trade / maxDD +4.13%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.1366 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: IRYS/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $298.55

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5488件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000371 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-24T03:31:03.576465+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=80935.3
- Funnel: target 1088 → liquid 166 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.9 >= 65=1, 4h RSI 66.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BMT/USDT:USDT | +92.47% | $1,271,965.72 |
| BIRB/USDT:USDT | +55.75% | $6,913,422.79 |
| IRYS/USDT:USDT | +41.80% | $100,976,771.47 |
| AXIS/USDT:USDT | +23.42% | $2,361,310.58 |
| AKE/USDT:USDT | +8.69% | $19,215,863.47 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NIL/USDT:USDT | below_1h_threshold | +4.47% | +4.50% |
| AGT/USDT:USDT | below_1h_threshold | +1.17% | +1.20% |
| BIRB/USDT:USDT | below_1h_threshold | +0.50% | +0.53% |
| SAMSUNGSTOCK/USDT:USDT | below_1h_threshold | +0.36% | +0.39% |
| MUSTOCK/USDT:USDT | below_1h_threshold | +0.33% | +0.37% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
