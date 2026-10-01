# Decision Report

- generated_at: 2026-10-01T16:56:44.912623+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15925**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15925, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.03%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.03% | **+0.03%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 5/20 | 25.0% | +5.92% | **+1.48%** |
| LIMIT_6PCT | 5/20 | 25.0% | +4.33% | **+1.08%** |
| LIMIT_8PCT | 3/20 | 15.0% | +6.57% | **+0.99%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.28% | **+0.51%** |
| LIMIT_FIB1272 | 2/20 | 10.0% | +4.58% | **+0.46%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +2.07% | **+1.45%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +1.78% | **+1.24%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.80% | **+0.76%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +0.80% | **+0.44%** |

## 2. $100 Live Portfolio

- 残高: **$120.63** / 初期 $100.00 (+20.63%)
- 確定トレード: 226件 (TP 82 / SL 137 / EXP 7)
- 最新: LONGXIA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.63
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,286.37** / 初期 $100.00 (+1186.37%)
- 確定: 6034件 (Win 1787 / Loss 1944 / Flat 2303) / skip 6452件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SI/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $1,286.37

## 4. Robust Adaptive DryRun ($100)

- 残高: **$276.47** / 初期 $100.00 (+176.47%)
- 確定: 3578件 (Win 996 / Loss 828 / Flat 1754) / skip 5758件
- 成長率目線: 平均log +0.000284 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1200 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SI/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $276.47

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4089件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000296 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-01T16:56:28.394866+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=84118.2
- Funnel: target 1097 → liquid 172 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 93.2 >= 65=1, 4h RSI 65.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MOVR/USDT:USDT | +10.88% | $24,594,382.80 |
| US/USDT:USDT | +4.96% | $1,482,180.48 |
| NOM/USDT:USDT | +3.49% | $3,083,768.36 |
| NIGHT/USDT:USDT | +2.82% | $10,869,774.37 |
| SNXX/USDT:USDT | +2.57% | $5,413,840.60 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NOM/USDT:USDT | below_1h_threshold | +3.42% | +3.43% |
| NIGHT/USDT:USDT | below_1h_threshold | +2.83% | +2.84% |
| ZRO/USDT:USDT | below_1h_threshold | +1.43% | +1.44% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +1.38% | +1.39% |
| MUU/USDT:USDT | below_1h_threshold | +1.22% | +1.23% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
