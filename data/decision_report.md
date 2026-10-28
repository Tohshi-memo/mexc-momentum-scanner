# Decision Report

- generated_at: 2026-10-28T20:56:33.120261+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17737**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.62% / filled 20/20。**
- 全期間 MARKET基準: n=17737, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.62%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.62% | **+0.62%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 11/20 | 55.0% | +2.02% | **+1.11%** |
| LIMIT_ATR | 12/20 | 60.0% | +1.63% | **+0.98%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.95% | **+0.86%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.89% | **+0.71%** |
| LIMIT_BB3S | 6/20 | 30.0% | +2.07% | **+0.62%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.63% | **+0.50%** |
| MARKET_LONG | 20/20 | 100.0% | +0.29% | **+0.29%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +1.13% | **+0.23%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | -0.04% | **-0.02%** |

## 2. $100 Live Portfolio

- 残高: **$121.62** / 初期 $100.00 (+21.62%)
- 確定トレード: 255件 (TP 94 / SL 153 / EXP 8)
- 最新: BTW/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.62
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,546.79** / 初期 $100.00 (+1446.79%)
- 確定: 6781件 (Win 1971 / Loss 2171 / Flat 2639) / skip 7517件
- 成長率目線: 平均log +0.000404 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: XPIN/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $1,546.79

## 4. Robust Adaptive DryRun ($100)

- 残高: **$359.08** / 初期 $100.00 (+259.08%)
- 確定: 4258件 (Win 1155 / Loss 969 / Flat 2134) / skip 6890件
- 成長率目線: 平均log +0.000300 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0402 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: XPIN/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $359.08

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5896件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000191 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-28T20:56:18.494166+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.47% price=81163.4
- Funnel: target 1083 → liquid 166 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| XPIN/USDT:USDT | +26.73% | $1,863,233.61 |
| AKE/USDT:USDT | +18.13% | $6,707,107.36 |
| Q/USDT:USDT | +15.03% | $27,609,360.45 |
| INIT/USDT:USDT | +10.31% | $1,988,115.77 |
| USELESS/USDT:USDT | +7.67% | $2,320,015.23 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MSTRSTOCK/USDT:USDT | below_1h_threshold | +3.11% | +3.58% |
| AGT/USDT:USDT | below_1h_threshold | +2.90% | +3.37% |
| SI/USDT:USDT | below_1h_threshold | +2.85% | +3.31% |
| IRENSTOCK/USDT:USDT | below_1h_threshold | +1.94% | +2.41% |
| AKE/USDT:USDT | below_1h_threshold | +1.72% | +2.19% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
