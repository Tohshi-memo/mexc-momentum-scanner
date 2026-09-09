# Decision Report

- generated_at: 2026-09-09T03:31:29.903955+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14028**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.43% / filled 20/20。**
- 全期間 MARKET基準: n=14028, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+2.43%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.43% | **+2.43%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.43% | **+2.43%** |
| LIMIT_1PCT | 18/20 | 90.0% | +2.14% | **+1.93%** |
| LIMIT_3PCT | 13/20 | 65.0% | +2.08% | **+1.35%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.78% | **+1.34%** |
| LIMIT_ATR | 12/20 | 60.0% | +1.83% | **+1.10%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +0.80% | **+0.40%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | -2.40% | **-0.36%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | -0.84% | **-0.51%** |
| MARKET_LONG | 20/20 | 100.0% | -0.59% | **-0.59%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,013.58** / 初期 $100.00 (+913.58%)
- 確定: 5292件 (Win 1588 / Loss 1707 / Flat 1997) / skip 5297件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: G/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $1,013.58

## 4. Robust Adaptive DryRun ($100)

- 残高: **$190.66** / 初期 $100.00 (+90.66%)
- 確定: 2631件 (Win 726 / Loss 622 / Flat 1283) / skip 4808件
- 成長率目線: 平均log +0.000245 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0470 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: G/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $190.66

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.48** / 初期 $100.00 (+19.48%)
- 確定: 2610件 (Win 764 / Loss 992 / Flat 854) / pending 2件 / skip 2887件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000321 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: G/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $119.48

## 6. Latest Market Context

- 更新: 2026-09-09T03:31:15.522492+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.16% price=78561.2
- Funnel: target 1070 → liquid 164 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| OL/USDT:USDT | +33.15% | $1,890,204.28 |
| CNPY/USDT:USDT | +15.62% | $1,036,142.79 |
| WAVES/USDT:USDT | +14.61% | $1,471,231.23 |
| ARX/USDT:USDT | +10.45% | $1,450,367.09 |
| SOFTBANKSTOCK/USDT:USDT | +6.73% | $7,559,890.96 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CNPY/USDT:USDT | below_1h_threshold | +3.05% | +3.21% |
| ACE/USDT:USDT | below_1h_threshold | +2.63% | +2.79% |
| OL/USDT:USDT | below_1h_threshold | +2.37% | +2.53% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.02% | +2.18% |
| KORU/USDT:USDT | below_1h_threshold | +1.48% | +1.64% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
