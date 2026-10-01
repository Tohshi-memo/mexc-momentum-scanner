# Decision Report

- generated_at: 2026-10-01T14:31:30.715428+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15907**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15907, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.94%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.94% | **-1.94%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 7/20 | 35.0% | +1.03% | **+0.36%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_FIB1272 | 3/20 | 15.0% | +0.95% | **+0.14%** |
| LIMIT_3PCT | 18/20 | 90.0% | +0.13% | **+0.12%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.04% | **+0.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 7/9 | 77.8% | +2.61% | **+2.03%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.91% | **+1.72%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +2.30% | **+1.38%** |
| MARKET_LONG | 20/20 | 100.0% | +1.09% | **+1.09%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +1.34% | **+0.74%** |

## 2. $100 Live Portfolio

- 残高: **$120.63** / 初期 $100.00 (+20.63%)
- 確定トレード: 226件 (TP 82 / SL 137 / EXP 7)
- 最新: LONGXIA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.63
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,307.59** / 初期 $100.00 (+1207.59%)
- 確定: 6022件 (Win 1784 / Loss 1936 / Flat 2302) / skip 6446件
- 成長率目線: 平均log +0.000427 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SYN/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.65% 残高後 $1,307.59

## 4. Robust Adaptive DryRun ($100)

- 残高: **$275.76** / 初期 $100.00 (+175.76%)
- 確定: 3560件 (Win 989 / Loss 818 / Flat 1753) / skip 5758件
- 成長率目線: 平均log +0.000285 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1351 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SYN/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.44% 残高後 $275.76

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4068件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000341 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-01T14:31:17.187771+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.22% price=84094.0
- Funnel: target 1097 → liquid 174 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=2, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LONGXIA/USDT:USDT | +74.59% | $7,055,319.53 |
| MOVR/USDT:USDT | +51.03% | $20,959,068.27 |
| CAP/USDT:USDT | +27.45% | $1,016,297.04 |
| CT/USDT:USDT | +26.29% | $7,108,338.49 |
| ACNSTOCK/USDT:USDT | +22.04% | $2,301,562.69 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SYN/USDT:USDT | below_relative_strength | +5.15% | +4.93% |
| CAP/USDT:USDT | below_relative_strength | +5.12% | +4.90% |
| ACNSTOCK/USDT:USDT | below_1h_threshold | +3.79% | +3.57% |
| MSTRSTOCK/USDT:USDT | below_1h_threshold | +2.21% | +2.00% |
| AAVE/USDT:USDT | below_1h_threshold | +2.10% | +1.88% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
