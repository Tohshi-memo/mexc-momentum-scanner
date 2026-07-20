# Decision Report

- generated_at: 2026-07-20T03:31:20.437776+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9079**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.17% / filled 20/20。**
- 全期間 MARKET基準: n=9079, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.17%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.17% | **+1.17%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.17% | **+1.17%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.19% | **+1.13%** |
| LIMIT_3PCT | 15/20 | 75.0% | +1.06% | **+0.80%** |
| LIMIT_ATR | 10/20 | 50.0% | +1.22% | **+0.61%** |
| LIMIT_BB3S | 2/18 | 11.1% | +5.43% | **+0.60%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +2.22% | **+0.44%** |
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.05% | **+0.05%** |
| MARKET_LONG | 20/20 | 100.0% | -0.03% | **-0.03%** |

## 2. $100 Live Portfolio

- 残高: **$109.69** / 初期 $100.00 (+9.69%)
- 確定トレード: 119件 (TP 43 / SL 71 / EXP 5)
- 最新: DEXE/USDT:USDT SL_HIT PnL -3.31% 残高後 $109.69
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$398.82** / 初期 $100.00 (+298.82%)
- 確定: 3141件 (Win 985 / Loss 1001 / Flat 1155) / skip 2499件
- 成長率目線: 平均log +0.000440 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $398.82

## 4. Robust Adaptive DryRun ($100)

- 残高: **$125.74** / 初期 $100.00 (+25.74%)
- 確定: 1040件 (Win 266 / Loss 218 / Flat 556) / skip 1450件
- 成長率目線: 平均log +0.000220 / 幾何平均 +0.022% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0440 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $125.74

## 5. Causal Adaptive DryRun ($100)

- 残高: **$100.90** / 初期 $100.00 (+0.90%)
- 確定: 278件 (Win 94 / Loss 131 / Flat 53) / pending 5件 / skip 268件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000179 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $100.90

## 6. Latest Market Context

- 更新: 2026-07-20T03:31:10.831225+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.25% price=64639.9
- Funnel: target 885 → liquid 133 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BANK/USDT:USDT | +50.22% | $90,363,080.11 |
| ACE/USDT:USDT | +46.71% | $3,535,738.48 |
| PUMPFUN/USDT:USDT | +18.85% | $17,269,762.49 |
| ESPORTS/USDT:USDT | +14.27% | $44,740,530.78 |
| PROM/USDT:USDT | +12.04% | $2,182,218.97 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| B/USDT:USDT | below_1h_threshold | +3.39% | +3.64% |
| VELVET/USDT:USDT | below_1h_threshold | +2.75% | +2.99% |
| SOXL/USDT:USDT | below_1h_threshold | +2.27% | +2.51% |
| ACE/USDT:USDT | below_1h_threshold | +1.63% | +1.88% |
| BEAT/USDT:USDT | below_1h_threshold | +1.33% | +1.57% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
