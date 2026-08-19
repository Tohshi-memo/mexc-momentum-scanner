# Decision Report

- generated_at: 2026-08-19T18:46:28.243165+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11996**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +3.78% / filled 20/20。**
- 全期間 MARKET基準: n=11996, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+3.78%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.78% | **+3.78%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.78% | **+3.78%** |
| LIMIT_1PCT | 12/20 | 60.0% | +1.59% | **+0.95%** |
| LIMIT_BB3S | 5/18 | 27.8% | +3.27% | **+0.91%** |
| LIMIT_2PCT | 10/20 | 50.0% | +0.91% | **+0.45%** |
| LIMIT_3PCT | 8/20 | 40.0% | +0.98% | **+0.39%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.24% | **+0.25%** |
| LIMIT_8PCT_LONG | 11/20 | 55.0% | +0.05% | **+0.03%** |
| LIMIT_7PCT_LONG | 12/20 | 60.0% | -1.19% | **-0.71%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | -3.01% | **-0.75%** |
| MARKET_LONG | 20/20 | 100.0% | -1.06% | **-1.06%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 188件 (TP 72 / SL 111 / EXP 5)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$605.47** / 初期 $100.00 (+505.47%)
- 確定: 4241件 (Win 1302 / Loss 1388 / Flat 1551) / skip 4316件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MUU/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $605.47

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.70** / 初期 $100.00 (+54.70%)
- 確定: 1821件 (Win 502 / Loss 428 / Flat 891) / skip 3586件
- 成長率目線: 平均log +0.000240 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: UNITREE/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.35% 残高後 $154.70

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.97** / 初期 $100.00 (+16.97%)
- 確定: 1753件 (Win 520 / Loss 669 / Flat 564) / pending 0件 / skip 1712件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000522 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: HEMI/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $116.97

## 6. Latest Market Context

- 更新: 2026-08-19T18:46:16.972690+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.35% price=68406.1
- Funnel: target 999 → liquid 193 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RE/USDT:USDT | +10.78% | $4,343,130.35 |
| BR/USDT:USDT | +9.55% | $2,595,496.73 |
| ON/USDT:USDT | +7.49% | $4,980,705.81 |
| WLD/USDT:USDT | +4.59% | $60,037,741.21 |
| USELESS/USDT:USDT | +4.50% | $1,284,841.82 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ACE/USDT:USDT | below_1h_threshold | +4.78% | +4.44% |
| HEMI/USDT:USDT | below_1h_threshold | +3.13% | +2.78% |
| 1000RATS/USDT:USDT | below_1h_threshold | +2.60% | +2.25% |
| EDEN/USDT:USDT | below_1h_threshold | +2.24% | +1.89% |
| RIVER/USDT:USDT | below_1h_threshold | +1.60% | +1.25% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
