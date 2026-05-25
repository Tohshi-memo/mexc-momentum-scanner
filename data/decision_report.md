# Decision Report

- generated_at: 2026-05-25T17:39:19.969583+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4865**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4865, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-0.99%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.99% | **-0.99%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 3/20 | 15.0% | +1.74% | **+0.26%** |
| LIMIT_7PCT | 4/20 | 20.0% | +0.87% | **+0.17%** |
| LIMIT_8PCT | 3/20 | 15.0% | +0.09% | **+0.01%** |
| LIMIT_10PCT | 3/20 | 15.0% | +0.09% | **+0.01%** |
| LIMIT_9PCT | 3/20 | 15.0% | +0.09% | **+0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 6/8 | 75.0% | +3.00% | **+2.25%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +3.03% | **+2.12%** |
| MARKET_LONG | 20/20 | 100.0% | +1.38% | **+1.38%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +2.39% | **+1.31%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +2.12% | **+1.27%** |

## 2. $100 Live Portfolio

- 残高: **$96.68** / 初期 $100.00 (-3.32%)
- 確定トレード: 63件 (TP 17 / SL 43 / EXP 3)
- 最新: KITE/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.68
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$128.59** / 初期 $100.00 (+28.59%)
- 確定: 671件 (Win 169 / Loss 212 / Flat 290) / skip 755件
- 成長率目線: 平均log +0.000375 / 幾何平均 +0.037% per trade / maxDD +4.72%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $128.59

## 4. Latest Market Context

- 更新: 2026-05-25T17:39:17.502330+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.16% price=77567.8
- Funnel: target 765 → liquid 123 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| POND/USDT:USDT | +78.57% | $1,186,617.72 |
| TONCOIN/USDT:USDT | +9.23% | $47,724,114.69 |
| NIL/USDT:USDT | +8.11% | $17,940,324.09 |
| H/USDT:USDT | +6.69% | $2,169,074.95 |
| TIA/USDT:USDT | +5.29% | $10,068,825.75 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LIT/USDT:USDT | below_1h_threshold | +4.27% | +4.43% |
| TONCOIN/USDT:USDT | below_1h_threshold | +3.74% | +3.90% |
| NIL/USDT:USDT | below_1h_threshold | +3.72% | +3.88% |
| GRASS/USDT:USDT | below_1h_threshold | +2.92% | +3.08% |
| H/USDT:USDT | below_1h_threshold | +2.41% | +2.57% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
