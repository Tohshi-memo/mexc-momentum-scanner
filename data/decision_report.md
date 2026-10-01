# Decision Report

- generated_at: 2026-10-01T11:56:31.804929+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15900**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15900, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-2.03%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.03% | **-2.03%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 9/20 | 45.0% | +0.95% | **+0.43%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_FIB1272 | 2/20 | 10.0% | +0.85% | **+0.09%** |
| LIMIT_4PCT | 15/20 | 75.0% | +0.05% | **+0.04%** |
| LIMIT_ATR | 17/20 | 85.0% | -0.27% | **-0.23%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 8/11 | 72.7% | +3.31% | **+2.41%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +2.51% | **+2.26%** |
| MARKET_LONG | 20/20 | 100.0% | +1.58% | **+1.58%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +2.28% | **+1.25%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +1.76% | **+0.88%** |

## 2. $100 Live Portfolio

- 残高: **$120.63** / 初期 $100.00 (+20.63%)
- 確定トレード: 226件 (TP 82 / SL 137 / EXP 7)
- 最新: LONGXIA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.63
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,296.94** / 初期 $100.00 (+1196.94%)
- 確定: 6017件 (Win 1782 / Loss 1935 / Flat 2300) / skip 6444件
- 成長率目線: 平均log +0.000426 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ACNSTOCK/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.00% 残高後 $1,296.94

## 4. Robust Adaptive DryRun ($100)

- 残高: **$272.83** / 初期 $100.00 (+172.83%)
- 確定: 3553件 (Win 985 / Loss 816 / Flat 1752) / skip 5758件
- 成長率目線: 平均log +0.000282 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1316 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LONGXIA/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $272.83

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4061件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000292 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-01T11:56:19.738486+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=83903.2
- Funnel: target 1097 → liquid 176 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 88.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MOVR/USDT:USDT | +69.41% | $17,888,335.18 |
| LONGXIA/USDT:USDT | +53.41% | $4,080,870.31 |
| NOM/USDT:USDT | +26.83% | $2,687,069.88 |
| CT/USDT:USDT | +21.31% | $6,748,179.81 |
| JASMY/USDT:USDT | +19.52% | $12,246,410.59 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MONAD/USDT:USDT | below_1h_threshold | +2.38% | +2.41% |
| TRB/USDT:USDT | below_1h_threshold | +1.89% | +1.92% |
| BR/USDT:USDT | below_1h_threshold | +1.62% | +1.65% |
| SYN/USDT:USDT | below_1h_threshold | +1.55% | +1.58% |
| KORU/USDT:USDT | below_1h_threshold | +1.47% | +1.50% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
