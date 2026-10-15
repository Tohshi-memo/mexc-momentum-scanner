# Decision Report

- generated_at: 2026-10-15T14:41:37.682121+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16745**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.36% / filled 20/20。**
- 全期間 MARKET基準: n=16745, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+2.36%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.36% | **+2.36%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.36% | **+2.36%** |
| LIMIT_1PCT | 16/20 | 80.0% | +1.26% | **+1.01%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_8PCT | 3/20 | 15.0% | +3.70% | **+0.56%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +2.00% | **+1.33%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +1.04% | **+0.57%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +0.11% | **+0.08%** |

## 2. $100 Live Portfolio

- 残高: **$121.48** / 初期 $100.00 (+21.48%)
- 確定トレード: 240件 (TP 89 / SL 144 / EXP 7)
- 最新: STRK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.48
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,267.30** / 初期 $100.00 (+1167.30%)
- 確定: 6311件 (Win 1849 / Loss 2025 / Flat 2437) / skip 6995件
- 成長率目線: 平均log +0.000402 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `MARKET` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RLC/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $1,267.30

## 4. Robust Adaptive DryRun ($100)

- 残高: **$274.10** / 初期 $100.00 (+174.10%)
- 確定: 3673件 (Win 1023 / Loss 871 / Flat 1779) / skip 6483件
- 成長率目線: 平均log +0.000275 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: 1000RATS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $274.10

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4906件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000390 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-15T14:41:25.084589+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +1.51% price=81381.2
- Funnel: target 1090 → liquid 187 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=45, below_relative_strength=4, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PUFFER/USDT:USDT | +83.64% | $2,140,616.81 |
| ZEREBRO/USDT:USDT | +35.91% | $8,825,248.92 |
| ARCSOL/USDT:USDT | +28.89% | $2,724,007.46 |
| SI/USDT:USDT | +18.67% | $2,014,512.33 |
| NIL/USDT:USDT | +17.29% | $17,543,097.88 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZRO/USDT:USDT | below_relative_strength | +6.24% | +4.73% |
| TIA/USDT:USDT | below_relative_strength | +5.28% | +3.77% |
| RLC/USDT:USDT | below_relative_strength | +5.28% | +3.77% |
| AVA/USDT:USDT | below_relative_strength | +5.14% | +3.64% |
| PYTH/USDT:USDT | below_1h_threshold | +4.96% | +3.45% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
