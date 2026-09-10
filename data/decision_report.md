# Decision Report

- generated_at: 2026-09-10T06:41:21.323538+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14155**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14155, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 5/20 | 25.0% | +5.42% | **+1.36%** |
| LIMIT_ATR | 12/20 | 60.0% | +1.65% | **+0.99%** |
| LIMIT_7PCT | 5/20 | 25.0% | +2.80% | **+0.70%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.89% | **+0.66%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +4.00% | **+3.00%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.57% | **+1.93%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +2.02% | **+1.82%** |
| MARKET_LONG | 20/20 | 100.0% | +1.60% | **+1.60%** |
| LIMIT_5PCT_LONG | 7/20 | 35.0% | +3.10% | **+1.08%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,059.01** / 初期 $100.00 (+959.01%)
- 確定: 5335件 (Win 1605 / Loss 1721 / Flat 2009) / skip 5381件
- 成長率目線: 平均log +0.000442 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BULLA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,059.01

## 4. Robust Adaptive DryRun ($100)

- 残高: **$207.46** / 初期 $100.00 (+107.46%)
- 確定: 2749件 (Win 761 / Loss 645 / Flat 1343) / skip 4817件
- 成長率目線: 平均log +0.000265 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0926 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BULLA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $207.46

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.14** / 初期 $100.00 (+22.14%)
- 確定: 2660件 (Win 785 / Loss 1015 / Flat 860) / pending 1件 / skip 2962件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000379 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BULLA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $122.14

## 6. Latest Market Context

- 更新: 2026-09-10T06:41:09.064695+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.39% price=78199.9
- Funnel: target 1064 → liquid 168 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 74.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VTHO/USDT:USDT | +49.65% | $3,518,776.37 |
| CATE/USDT:USDT | +34.31% | $2,778,032.44 |
| VET/USDT:USDT | +6.73% | $5,701,279.88 |
| REZ/USDT:USDT | +6.65% | $1,044,407.85 |
| KAS/USDT:USDT | +5.02% | $4,517,432.98 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTR/USDT:USDT | below_1h_threshold | +3.00% | +3.39% |
| VTHO/USDT:USDT | below_1h_threshold | +2.58% | +2.97% |
| EGLD/USDT:USDT | below_1h_threshold | +1.01% | +1.40% |
| MINA/USDT:USDT | below_1h_threshold | +0.94% | +1.33% |
| ETHFI/USDT:USDT | below_1h_threshold | +0.87% | +1.25% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
