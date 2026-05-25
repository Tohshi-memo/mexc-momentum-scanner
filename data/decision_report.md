# Decision Report

- generated_at: 2026-05-25T18:04:18.502574+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4867**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4867, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-0.39%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.39% | **-0.39%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 5/20 | 25.0% | +1.26% | **+0.31%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +1.74% | **+0.26%** |
| LIMIT_9PCT | 4/20 | 20.0% | +1.22% | **+0.24%** |
| LIMIT_8PCT | 4/20 | 20.0% | +1.00% | **+0.20%** |
| ASK | 20/20 | 100.0% | +0.17% | **+0.17%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 7/9 | 77.8% | +2.00% | **+1.56%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.59% | **+1.11%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.41% | **+0.91%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +1.25% | **+0.87%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +1.17% | **+0.58%** |

## 2. $100 Live Portfolio

- 残高: **$96.68** / 初期 $100.00 (-3.32%)
- 確定トレード: 63件 (TP 17 / SL 43 / EXP 3)
- 最新: KITE/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.68
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$127.31** / 初期 $100.00 (+27.31%)
- 確定: 673件 (Win 169 / Loss 214 / Flat 290) / skip 755件
- 成長率目線: 平均log +0.000359 / 幾何平均 +0.036% per trade / maxDD +4.72%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: IN/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $127.31

## 4. Latest Market Context

- 更新: 2026-05-25T18:04:16.369098+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=77560.6
- Funnel: target 765 → liquid 122 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| POND/USDT:USDT | +72.85% | $1,236,927.17 |
| NIL/USDT:USDT | +12.72% | $17,070,541.30 |
| PHA/USDT:USDT | +10.34% | $3,710,270.55 |
| H/USDT:USDT | +8.24% | $2,236,940.95 |
| TIA/USDT:USDT | +7.62% | $11,697,449.50 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| INJ/USDT:USDT | below_1h_threshold | +1.51% | +1.46% |
| LIT/USDT:USDT | below_1h_threshold | +1.30% | +1.26% |
| FET/USDT:USDT | below_1h_threshold | +1.17% | +1.13% |
| TIA/USDT:USDT | below_1h_threshold | +1.12% | +1.08% |
| TONCOIN/USDT:USDT | below_1h_threshold | +0.99% | +0.94% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
