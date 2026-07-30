# Decision Report

- generated_at: 2026-07-30T20:36:26.976347+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9923**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9923, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-2.93%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.93% | **-2.93%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_7PCT | 4/20 | 20.0% | +5.40% | **+1.08%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.94% | **+0.39%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.20% | **+0.06%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | -0.26% | **-0.13%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +3.53% | **+3.17%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +4.29% | **+3.00%** |
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +2.43% | **+2.43%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +3.32% | **+2.32%** |
| MARKET_LONG | 20/20 | 100.0% | +2.32% | **+2.32%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$507.16** / 初期 $100.00 (+407.16%)
- 確定: 3523件 (Win 1116 / Loss 1147 / Flat 1260) / skip 2961件
- 成長率目線: 平均log +0.000461 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +1.00% 残高後 $507.16

## 4. Robust Adaptive DryRun ($100)

- 残高: **$136.91** / 初期 $100.00 (+36.91%)
- 確定: 1243件 (Win 344 / Loss 283 / Flat 616) / skip 2091件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1339 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KOMA/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $136.91

## 5. Causal Adaptive DryRun ($100)

- 残高: **$110.61** / 初期 $100.00 (+10.61%)
- 確定: 804件 (Win 262 / Loss 319 / Flat 223) / pending 1件 / skip 596件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000174 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SNXX/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $110.61

## 6. Latest Market Context

- 更新: 2026-07-30T20:36:19.710913+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=64764.8
- Funnel: target 920 → liquid 180 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AXTISTOCK/USDT:USDT | +33.81% | $1,104,360.58 |
| MMT/USDT:USDT | +20.24% | $6,402,019.48 |
| ESPORTS/USDT:USDT | +17.21% | $4,579,439.56 |
| ROBO/USDT:USDT | +15.26% | $2,897,798.00 |
| AMZU/USDT:USDT | +14.61% | $2,637,294.69 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SNXX/USDT:USDT | below_1h_threshold | +3.97% | +3.98% |
| KIOXIASTOCK/USDT:USDT | below_1h_threshold | +3.45% | +3.46% |
| KORU/USDT:USDT | below_1h_threshold | +3.23% | +3.24% |
| STXSTOCK/USDT:USDT | below_1h_threshold | +2.10% | +2.11% |
| INFQSTOCK/USDT:USDT | below_1h_threshold | +2.04% | +2.05% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
