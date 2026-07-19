# Decision Report

- generated_at: 2026-07-19T18:16:03.094090+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9064**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.41% / filled 20/20。**
- 全期間 MARKET基準: n=9064, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.41%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.41% | **+1.41%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.41% | **+1.41%** |
| LIMIT_7PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_5PCT | 5/20 | 25.0% | +2.36% | **+0.59%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_FIB1272 | 3/20 | 15.0% | +1.74% | **+0.26%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +4.55% | **+1.36%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +6.07% | **+0.91%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +1.65% | **+0.83%** |
| MARKET_LONG | 20/20 | 100.0% | +0.18% | **+0.18%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.09% | **+0.07%** |

## 2. $100 Live Portfolio

- 残高: **$109.69** / 初期 $100.00 (+9.69%)
- 確定トレード: 119件 (TP 43 / SL 71 / EXP 5)
- 最新: DEXE/USDT:USDT SL_HIT PnL -3.31% 残高後 $109.69
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$401.25** / 初期 $100.00 (+301.25%)
- 確定: 3126件 (Win 982 / Loss 999 / Flat 1145) / skip 2499件
- 成長率目線: 平均log +0.000444 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BANK/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $401.25

## 4. Robust Adaptive DryRun ($100)

- 残高: **$125.55** / 初期 $100.00 (+25.55%)
- 確定: 1025件 (Win 264 / Loss 218 / Flat 543) / skip 1450件
- 成長率目線: 平均log +0.000222 / 幾何平均 +0.022% per trade / maxDD +3.89%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0914 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BANK/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $125.55

## 5. Causal Adaptive DryRun ($100)

- 残高: **$100.97** / 初期 $100.00 (+0.97%)
- 確定: 264件 (Win 91 / Loss 130 / Flat 43) / pending 3件 / skip 268件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000216 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BANK/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $100.97

## 6. Latest Market Context

- 更新: 2026-07-19T18:15:58.692458+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.12% price=64442.8
- Funnel: target 885 → liquid 128 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BANK/USDT:USDT | +23.43% | $60,693,446.72 |
| B/USDT:USDT | +10.97% | $36,272,175.96 |
| DEXE/USDT:USDT | +8.53% | $1,464,085.38 |
| ESPORTS/USDT:USDT | +6.75% | $62,023,692.02 |
| TLM/USDT:USDT | +5.37% | $12,289,337.54 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TRADOOR/USDT:USDT | below_1h_threshold | +2.55% | +2.67% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +1.02% | +1.14% |
| ESPORTS/USDT:USDT | below_1h_threshold | +0.94% | +1.06% |
| B/USDT:USDT | below_1h_threshold | +0.93% | +1.05% |
| SAMSUNGSTOCK/USDT:USDT | below_1h_threshold | +0.62% | +0.74% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
