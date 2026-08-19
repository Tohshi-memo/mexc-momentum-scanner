# Decision Report

- generated_at: 2026-08-19T14:26:25.157317+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11982**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +3.77% / filled 20/20。**
- 全期間 MARKET基準: n=11982, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+3.77%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.77% | **+3.77%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.77% | **+3.77%** |
| LIMIT_1PCT | 12/20 | 60.0% | +1.74% | **+1.04%** |
| LIMIT_BB3S | 4/19 | 21.1% | +3.58% | **+0.75%** |
| LIMIT_2PCT | 9/20 | 45.0% | +0.32% | **+0.15%** |
| LIMIT_4PCT | 5/20 | 25.0% | +0.00% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +0.15% | **+0.02%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | -0.04% | **-0.01%** |
| LIMIT_8PCT_LONG | 11/20 | 55.0% | -0.31% | **-0.17%** |
| LIMIT_FIB1618_LONG | 6/20 | 30.0% | -2.49% | **-0.75%** |
| LIMIT_7PCT_LONG | 12/20 | 60.0% | -1.43% | **-0.86%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 188件 (TP 72 / SL 111 / EXP 5)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$605.47** / 初期 $100.00 (+505.47%)
- 確定: 4241件 (Win 1302 / Loss 1388 / Flat 1551) / skip 4302件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MUU/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $605.47

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.70** / 初期 $100.00 (+54.70%)
- 確定: 1821件 (Win 502 / Loss 428 / Flat 891) / skip 3572件
- 成長率目線: 平均log +0.000240 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: UNITREE/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.35% 残高後 $154.70

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.97** / 初期 $100.00 (+16.97%)
- 確定: 1753件 (Win 520 / Loss 669 / Flat 564) / pending 0件 / skip 1700件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000263 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: HEMI/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $116.97

## 6. Latest Market Context

- 更新: 2026-08-19T14:26:16.622921+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.59% price=65367.9
- Funnel: target 997 → liquid 185 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +74.48% | $112,312,614.57 |
| HEMI/USDT:USDT | +37.92% | $5,796,213.99 |
| STAR/USDT:USDT | +27.76% | $1,092,429.95 |
| UNITREE/USDT:USDT | +19.04% | $17,825,415.41 |
| DOS/USDT:USDT | +14.73% | $1,496,360.66 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CRCLSTOCK/USDT:USDT | below_1h_threshold | +4.30% | +3.71% |
| MSTRSTOCK/USDT:USDT | below_1h_threshold | +2.85% | +2.26% |
| EDEN/USDT:USDT | below_1h_threshold | +2.77% | +2.18% |
| SQQQ/USDT:USDT | below_1h_threshold | +2.47% | +1.88% |
| AAPLSTOCK/USDT:USDT | below_1h_threshold | +1.80% | +1.21% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
