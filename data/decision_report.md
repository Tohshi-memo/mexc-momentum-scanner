# Decision Report

- generated_at: 2026-08-22T03:51:41.778563+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12303**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12303, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-2.09%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.09% | **-2.09%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 5/20 | 25.0% | +2.05% | **+0.51%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_4PCT | 16/20 | 80.0% | -0.00% | **-0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/6 | 66.7% | +5.39% | **+3.59%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +2.86% | **+2.58%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +3.50% | **+1.92%** |
| MARKET_LONG | 20/20 | 100.0% | +1.80% | **+1.80%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +2.90% | **+1.45%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 190件 (TP 72 / SL 113 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$713.84** / 初期 $100.00 (+613.84%)
- 確定: 4421件 (Win 1355 / Loss 1442 / Flat 1624) / skip 4443件
- 成長率目線: 平均log +0.000445 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TRUMPOFFICIAL/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $713.84

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.76** / 初期 $100.00 (+56.76%)
- 確定: 1909件 (Win 526 / Loss 455 / Flat 928) / skip 3805件
- 成長率目線: 平均log +0.000235 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.2773 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TRUMPOFFICIAL/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $156.76

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.59** / 初期 $100.00 (+18.59%)
- 確定: 1849件 (Win 548 / Loss 696 / Flat 605) / pending 6件 / skip 1933件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000603 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: TRUMPOFFICIAL/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $118.59

## 6. Latest Market Context

- 更新: 2026-08-22T03:51:26.837405+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.17% price=78598.0
- Funnel: target 1018 → liquid 221 → pre 50 → checked 50 → surge 5 → strict 1
- Surge前reject: below_1h_threshold=45, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.2 >= 65=1, 4h RSI 75.2 >= 65=1, 4h RSI 88.1 >= 65=1, 4h RSI 88.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BASECAT/USDT:USDT | +238.76% | $4,168,176.38 |
| CATE/USDT:USDT | +74.00% | $11,987,086.95 |
| TRUMPOFFICIAL/USDT:USDT | +32.14% | $24,918,036.25 |
| MUBARAK/USDT:USDT | +31.76% | $1,313,519.50 |
| ZEC/USDT:USDT | +29.02% | $327,612,728.81 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| OP/USDT:USDT | below_1h_threshold | +4.14% | +3.98% |
| BASED/USDT:USDT | below_1h_threshold | +3.67% | +3.50% |
| ZEC/USDT:USDT | below_1h_threshold | +3.23% | +3.06% |
| APE/USDT:USDT | below_1h_threshold | +3.06% | +2.89% |
| SPX/USDT:USDT | below_1h_threshold | +3.04% | +2.87% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
