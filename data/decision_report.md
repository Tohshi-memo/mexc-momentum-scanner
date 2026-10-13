# Decision Report

- generated_at: 2026-10-13T18:46:27.621875+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16647**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.44% / filled 20/20。**
- 全期間 MARKET基準: n=16647, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.44%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.44% | **+0.44%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.44% | **+0.44%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_FIB1618 | 4/20 | 20.0% | +0.57% | **+0.11%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 7/7 | 100.0% | +1.69% | **+1.69%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.74% | **+1.39%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +1.54% | **+0.92%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.86% | **+0.56%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +2.42% | **+0.48%** |

## 2. $100 Live Portfolio

- 残高: **$121.72** / 初期 $100.00 (+21.72%)
- 確定トレード: 238件 (TP 89 / SL 142 / EXP 7)
- 最新: BATON/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.72
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,285.29** / 初期 $100.00 (+1185.29%)
- 確定: 6295件 (Win 1845 / Loss 2017 / Flat 2433) / skip 6913件
- 成長率目線: 平均log +0.000406 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: OGN/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $1,285.29

## 4. Robust Adaptive DryRun ($100)

- 残高: **$270.76** / 初期 $100.00 (+170.76%)
- 確定: 3654件 (Win 1015 / Loss 864 / Flat 1775) / skip 6404件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MAGIC/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $270.76

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4809件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000174 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-13T18:46:15.255331+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=83054.9
- Funnel: target 1094 → liquid 191 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ARCSOL/USDT:USDT | +16.08% | $1,794,095.44 |
| BATON/USDT:USDT | +7.10% | $1,463,633.59 |
| QNT/USDT:USDT | +6.61% | $104,079,096.69 |
| LONGXIA/USDT:USDT | +6.37% | $1,927,097.37 |
| OP/USDT:USDT | +5.55% | $16,276,255.22 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NIL/USDT:USDT | below_1h_threshold | +4.14% | +4.15% |
| SAFE/USDT:USDT | below_1h_threshold | +2.28% | +2.29% |
| ARCSOL/USDT:USDT | below_1h_threshold | +2.24% | +2.25% |
| OP/USDT:USDT | below_1h_threshold | +2.15% | +2.16% |
| LONGXIA/USDT:USDT | below_1h_threshold | +1.84% | +1.85% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
