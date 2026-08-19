# Decision Report

- generated_at: 2026-08-19T21:16:18.714420+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11998**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.70% / filled 20/20。**
- 全期間 MARKET基準: n=11998, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+2.70%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.70% | **+2.70%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.70% | **+2.70%** |
| LIMIT_BB3S | 5/17 | 29.4% | +3.27% | **+0.96%** |
| LIMIT_1PCT | 14/20 | 70.0% | +0.90% | **+0.63%** |
| LIMIT_3PCT | 10/20 | 50.0% | +1.19% | **+0.59%** |
| LIMIT_5PCT | 5/20 | 25.0% | +1.76% | **+0.44%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.29% | **+0.19%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +0.06% | **+0.03%** |
| MARKET_LONG | 20/20 | 100.0% | -0.24% | **-0.24%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | -0.56% | **-0.48%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | -3.33% | **-0.50%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 188件 (TP 72 / SL 111 / EXP 5)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$605.47** / 初期 $100.00 (+505.47%)
- 確定: 4241件 (Win 1302 / Loss 1388 / Flat 1551) / skip 4318件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MUU/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $605.47

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.70** / 初期 $100.00 (+54.70%)
- 確定: 1821件 (Win 502 / Loss 428 / Flat 891) / skip 3588件
- 成長率目線: 平均log +0.000240 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: UNITREE/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.35% 残高後 $154.70

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.97** / 初期 $100.00 (+16.97%)
- 確定: 1753件 (Win 520 / Loss 669 / Flat 564) / pending 0件 / skip 1717件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000514 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: HEMI/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $116.97

## 6. Latest Market Context

- 更新: 2026-08-19T21:16:11.809373+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.62% price=69447.0
- Funnel: target 999 → liquid 197 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 89.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BASECAT/USDT:USDT | +31.30% | $1,030,008.30 |
| MRNASTOCK/USDT:USDT | +29.65% | $3,318,051.42 |
| MAGMA/USDT:USDT | +25.56% | $1,433,294.80 |
| TRUMPOFFICIAL/USDT:USDT | +16.50% | $4,841,432.06 |
| RE/USDT:USDT | +15.47% | $7,073,090.29 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BASECAT/USDT:USDT | below_1h_threshold | +4.69% | +4.07% |
| ARB/USDT:USDT | below_1h_threshold | +3.39% | +2.77% |
| USELESS/USDT:USDT | below_1h_threshold | +3.32% | +2.70% |
| FILECOIN/USDT:USDT | below_1h_threshold | +2.87% | +2.25% |
| SOL/USDT:USDT | below_1h_threshold | +2.80% | +2.17% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
