# Decision Report

- generated_at: 2026-08-19T19:31:33.306773+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11997**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +3.25% / filled 20/20。**
- 全期間 MARKET基準: n=11997, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+3.25%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.25% | **+3.25%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.25% | **+3.25%** |
| LIMIT_BB3S | 5/17 | 29.4% | +3.27% | **+0.96%** |
| LIMIT_1PCT | 13/20 | 65.0% | +1.27% | **+0.83%** |
| LIMIT_3PCT | 9/20 | 45.0% | +1.43% | **+0.64%** |
| LIMIT_5PCT | 4/20 | 20.0% | +1.97% | **+0.39%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.29% | **+0.19%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +0.06% | **+0.03%** |
| LIMIT_7PCT_LONG | 11/20 | 55.0% | -0.93% | **-0.51%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | -2.77% | **-0.55%** |
| MARKET_LONG | 20/20 | 100.0% | -0.61% | **-0.61%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 188件 (TP 72 / SL 111 / EXP 5)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$605.47** / 初期 $100.00 (+505.47%)
- 確定: 4241件 (Win 1302 / Loss 1388 / Flat 1551) / skip 4317件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MUU/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $605.47

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.70** / 初期 $100.00 (+54.70%)
- 確定: 1821件 (Win 502 / Loss 428 / Flat 891) / skip 3587件
- 成長率目線: 平均log +0.000240 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: UNITREE/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.35% 残高後 $154.70

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.97** / 初期 $100.00 (+16.97%)
- 確定: 1753件 (Win 520 / Loss 669 / Flat 564) / pending 0件 / skip 1715件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000522 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: HEMI/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $116.97

## 6. Latest Market Context

- 更新: 2026-08-19T19:31:23.856079+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.39% price=68103.0
- Funnel: target 999 → liquid 193 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.6 >= 65=1, 4h RSI 75.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RE/USDT:USDT | +16.30% | $5,250,983.45 |
| HYPE/USDT:USDT | +11.17% | $301,872,930.30 |
| ON/USDT:USDT | +9.95% | $4,913,803.49 |
| BR/USDT:USDT | +8.92% | $2,736,813.96 |
| LIT/USDT:USDT | +7.62% | $3,923,339.31 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NIL/USDT:USDT | below_1h_threshold | +4.70% | +5.08% |
| RE/USDT:USDT | below_1h_threshold | +4.39% | +4.78% |
| ARB/USDT:USDT | below_1h_threshold | +2.33% | +2.72% |
| TIA/USDT:USDT | below_1h_threshold | +2.07% | +2.45% |
| AVNT/USDT:USDT | below_1h_threshold | +2.06% | +2.45% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
