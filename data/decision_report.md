# Decision Report

- generated_at: 2026-09-08T16:21:25.267919+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14011**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.24% / filled 20/20。**
- 全期間 MARKET基準: n=14011, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.24%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.24% | **+0.24%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 5/20 | 25.0% | +1.01% | **+0.25%** |
| MARKET | 20/20 | 100.0% | +0.24% | **+0.24%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.06% | **+0.04%** |
| LIMIT_FIB1272 | 3/20 | 15.0% | +0.17% | **+0.03%** |
| LIMIT_1PCT | 17/20 | 85.0% | -0.65% | **-0.55%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.16% | **+1.16%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.28% | **+1.09%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +2.25% | **+0.67%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.73% | **+0.48%** |
| LIMIT_BB3S_LONG | 2/6 | 33.3% | +0.58% | **+0.19%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,010.80** / 初期 $100.00 (+910.80%)
- 確定: 5275件 (Win 1586 / Loss 1707 / Flat 1982) / skip 5297件
- 成長率目線: 平均log +0.000439 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BNCSTOCK/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $1,010.80

## 4. Robust Adaptive DryRun ($100)

- 残高: **$190.34** / 初期 $100.00 (+90.34%)
- 確定: 2614件 (Win 724 / Loss 622 / Flat 1268) / skip 4808件
- 成長率目線: 平均log +0.000246 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0381 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BNCSTOCK/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $190.34

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.92** / 初期 $100.00 (+19.92%)
- 確定: 2598件 (Win 761 / Loss 985 / Flat 852) / pending 3件 / skip 2883件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000184 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: USELESS/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $119.92

## 6. Latest Market Context

- 更新: 2026-09-08T16:21:13.292206+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.39% price=78557.4
- Funnel: target 1070 → liquid 159 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BNCSTOCK/USDT:USDT | +4.41% | $2,493,730.22 |
| BONER/USDT:USDT | +3.58% | $2,277,838.18 |
| PONS/USDT:USDT | +2.92% | $7,335,179.77 |
| UAI/USDT:USDT | +1.96% | $16,158,032.58 |
| LIT/USDT:USDT | +1.16% | $5,006,630.77 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BONER/USDT:USDT | below_1h_threshold | +3.51% | +3.90% |
| PONS/USDT:USDT | below_1h_threshold | +2.92% | +3.32% |
| UAI/USDT:USDT | below_1h_threshold | +1.95% | +2.34% |
| MUU/USDT:USDT | below_1h_threshold | +1.51% | +1.90% |
| AMDSTOCK/USDT:USDT | below_1h_threshold | +1.41% | +1.80% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
