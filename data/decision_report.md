# Decision Report

- generated_at: 2026-09-29T20:26:32.700165+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15797**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15797, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.09%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.09% | **-1.09%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 14/20 | 70.0% | +1.52% | **+1.07%** |
| LIMIT_7PCT | 7/20 | 35.0% | +2.86% | **+1.00%** |
| LIMIT_6PCT | 8/20 | 40.0% | +2.00% | **+0.80%** |
| LIMIT_5PCT | 11/20 | 55.0% | +1.26% | **+0.70%** |
| LIMIT_8PCT | 6/20 | 30.0% | +2.00% | **+0.60%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +4.00% | **+3.00%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +3.24% | **+2.27%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +2.45% | **+2.08%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.78% | **+1.69%** |
| MARKET_LONG | 20/20 | 100.0% | +0.66% | **+0.66%** |

## 2. $100 Live Portfolio

- 残高: **$120.75** / 初期 $100.00 (+20.75%)
- 確定トレード: 225件 (TP 82 / SL 136 / EXP 7)
- 最新: XLM/USDT:USDT SL_HIT PnL -2.52% 残高後 $120.75
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,227.24** / 初期 $100.00 (+1127.24%)
- 確定: 5987件 (Win 1766 / Loss 1925 / Flat 2296) / skip 6371件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GRASS/USDT:USDT `LIMIT_BB3S` EXPIRED account +0.00% 残高後 $1,227.24

## 4. Robust Adaptive DryRun ($100)

- 残高: **$263.08** / 初期 $100.00 (+163.08%)
- 確定: 3535件 (Win 974 / Loss 812 / Flat 1749) / skip 5673件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0588 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SI/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $263.08

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 3960件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000305 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-09-29T20:26:21.158136+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=83570.4
- Funnel: target 1073 → liquid 164 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 88.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SI/USDT:USDT | +121.81% | $2,715,996.99 |
| GRASS/USDT:USDT | +15.33% | $10,929,041.15 |
| QNT/USDT:USDT | +6.39% | $331,882,161.00 |
| SOONNETWORK/USDT:USDT | +5.83% | $2,894,801.94 |
| NIL/USDT:USDT | +5.59% | $2,538,866.98 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GRASS/USDT:USDT | below_1h_threshold | +4.59% | +4.58% |
| ICP/USDT:USDT | below_1h_threshold | +2.87% | +2.85% |
| PYTH/USDT:USDT | below_1h_threshold | +1.97% | +1.96% |
| SAND/USDT:USDT | below_1h_threshold | +1.97% | +1.96% |
| FARTCOIN/USDT:USDT | below_1h_threshold | +1.92% | +1.90% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
