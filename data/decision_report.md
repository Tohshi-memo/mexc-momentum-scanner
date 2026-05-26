# Decision Report

- generated_at: 2026-05-26T22:14:17.559023+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4909**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.71% / filled 20/20。**
- 全期間 MARKET基準: n=4909, expectancy=-0.08%
- 直近20件 MARKET基準: n=20, expectancy=+0.71%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.71% | **+0.71%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.71% | **+0.71%** |
| ASK | 20/20 | 100.0% | +0.65% | **+0.65%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.50% | **+0.45%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +2.97% | **+2.23%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +1.40% | **+1.05%** |
| LIMIT_ATR_LONG | 16/20 | 80.0% | +0.56% | **+0.45%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.41% | **+0.39%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.22% | **+0.33%** |

## 2. $100 Live Portfolio

- 残高: **$97.16** / 初期 $100.00 (-2.84%)
- 確定トレード: 65件 (TP 18 / SL 44 / EXP 3)
- 最新: ESPORTS/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.16
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$130.01** / 初期 $100.00 (+30.01%)
- 確定: 678件 (Win 172 / Loss 215 / Flat 291) / skip 792件
- 成長率目線: 平均log +0.000387 / 幾何平均 +0.039% per trade / maxDD +4.72%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PHA/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.61% 残高後 $130.01

## 4. Latest Market Context

- 更新: 2026-05-26T22:14:15.143448+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=75821.7
- Funnel: target 766 → liquid 137 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LUNC/USDT:USDT | +9.11% | $3,352,166.56 |
| ESPORTS/USDT:USDT | +7.30% | $8,598,913.09 |
| PLAY/USDT:USDT | +6.74% | $7,351,892.63 |
| MYX/USDT:USDT | +5.44% | $1,233,426.38 |
| BILL/USDT:USDT | +4.48% | $7,885,659.01 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PLAY/USDT:USDT | below_1h_threshold | +1.53% | +1.59% |
| TONCOIN/USDT:USDT | below_1h_threshold | +1.27% | +1.33% |
| LUNC/USDT:USDT | below_1h_threshold | +1.27% | +1.32% |
| UB/USDT:USDT | below_1h_threshold | +1.25% | +1.31% |
| IO/USDT:USDT | below_1h_threshold | +1.22% | +1.28% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
