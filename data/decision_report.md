# Decision Report

- generated_at: 2026-09-14T06:11:26.765704+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14490**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14490, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.78%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.78% | **-0.78%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 20/20 | 100.0% | +0.94% | **+0.94%** |
| LIMIT_5PCT | 6/20 | 30.0% | +2.13% | **+0.64%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.52% | **+0.42%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +0.63% | **+0.31%** |
| LIMIT_1PCT | 20/20 | 100.0% | +0.28% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +2.77% | **+1.38%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +3.49% | **+1.22%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +1.16% | **+0.52%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +1.20% | **+0.48%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 211件 (TP 78 / SL 128 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,072.66** / 初期 $100.00 (+972.66%)
- 確定: 5434件 (Win 1635 / Loss 1762 / Flat 2037) / skip 5617件
- 成長率目線: 平均log +0.000437 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PUNDIX/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.22% 残高後 $1,072.66

## 4. Robust Adaptive DryRun ($100)

- 残高: **$227.62** / 初期 $100.00 (+127.62%)
- 確定: 2991件 (Win 830 / Loss 716 / Flat 1445) / skip 4910件
- 成長率目線: 平均log +0.000275 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0126 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $227.62

## 5. Causal Adaptive DryRun ($100)

- 残高: **$126.02** / 初期 $100.00 (+26.02%)
- 確定: 2871件 (Win 854 / Loss 1112 / Flat 905) / pending 5件 / skip 3086件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000121 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: 4/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $126.02

## 6. Latest Market Context

- 更新: 2026-09-14T06:11:18.850296+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.24% price=77760.1
- Funnel: target 1068 → liquid 144 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=1, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +39.55% | $1,666,232.01 |
| MTL/USDT:USDT | +38.90% | $1,405,227.21 |
| BR/USDT:USDT | +31.23% | $4,407,523.04 |
| ARK/USDT:USDT | +26.95% | $4,171,325.86 |
| BTW/USDT:USDT | +14.78% | $11,980,133.20 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ARK/USDT:USDT | below_relative_strength | +5.05% | +4.81% |
| POWR/USDT:USDT | below_1h_threshold | +3.09% | +2.85% |
| FILECOIN/USDT:USDT | below_1h_threshold | +2.93% | +2.69% |
| BR/USDT:USDT | below_1h_threshold | +1.60% | +1.36% |
| NEAR/USDT:USDT | below_1h_threshold | +1.50% | +1.26% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
