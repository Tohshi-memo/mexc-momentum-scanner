# Decision Report

- generated_at: 2026-10-02T06:51:25.812971+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15975**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15975, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.03%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.03% | **-0.03%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 9/20 | 45.0% | +2.13% | **+0.96%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.45% | **+0.94%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.06% | **+0.85%** |
| LIMIT_8PCT | 3/20 | 15.0% | +5.14% | **+0.77%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +2.32% | **+0.70%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.30% | **+0.65%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +1.02% | **+0.51%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +1.28% | **+0.45%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.57% | **+0.43%** |

## 2. $100 Live Portfolio

- 残高: **$120.51** / 初期 $100.00 (+20.51%)
- 確定トレード: 227件 (TP 82 / SL 138 / EXP 7)
- 最新: BATON/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.51
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,309.37** / 初期 $100.00 (+1209.37%)
- 確定: 6080件 (Win 1801 / Loss 1957 / Flat 2322) / skip 6456件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BATON/USDT:USDT `LIMIT_FIB1272` SL_HIT account +0.15% 残高後 $1,309.37

## 4. Robust Adaptive DryRun ($100)

- 残高: **$275.42** / 初期 $100.00 (+175.42%)
- 確定: 3604件 (Win 1005 / Loss 844 / Flat 1755) / skip 5782件
- 成長率目線: 平均log +0.000281 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0247 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MAGMA/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $275.42

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4134件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000256 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-02T06:51:16.187637+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=85992.6
- Funnel: target 1098 → liquid 172 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BATON/USDT:USDT | +95.57% | $3,672,130.79 |
| MAGMA/USDT:USDT | +26.05% | $1,987,808.33 |
| SUPER/USDT:USDT | +13.15% | $1,116,080.12 |
| ZRO/USDT:USDT | +12.33% | $12,889,766.67 |
| CT/USDT:USDT | +12.06% | $7,912,413.65 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TIA/USDT:USDT | below_1h_threshold | +3.97% | +3.93% |
| MONAD/USDT:USDT | below_1h_threshold | +3.23% | +3.20% |
| SAND/USDT:USDT | below_1h_threshold | +3.10% | +3.07% |
| WLD/USDT:USDT | below_1h_threshold | +2.65% | +2.62% |
| MAGMA/USDT:USDT | below_1h_threshold | +2.52% | +2.49% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
