# Decision Report

- generated_at: 2026-05-25T17:24:21.457074+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4864**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4864, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-1.59%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.59% | **-1.59%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 4/20 | 20.0% | +1.30% | **+0.26%** |
| LIMIT_7PCT | 4/20 | 20.0% | +0.87% | **+0.17%** |
| LIMIT_8PCT | 3/20 | 15.0% | +0.09% | **+0.01%** |
| LIMIT_10PCT | 3/20 | 15.0% | +0.09% | **+0.01%** |
| LIMIT_9PCT | 3/20 | 15.0% | +0.09% | **+0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +3.76% | **+2.63%** |
| LIMIT_BB3S_LONG | 6/8 | 75.0% | +3.00% | **+2.25%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +3.41% | **+1.87%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +2.72% | **+1.63%** |
| ASK_LONG | 20/20 | 100.0% | +1.47% | **+1.47%** |

## 2. $100 Live Portfolio

- 残高: **$96.68** / 初期 $100.00 (-3.32%)
- 確定トレード: 63件 (TP 17 / SL 43 / EXP 3)
- 最新: KITE/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.68
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$129.24** / 初期 $100.00 (+29.24%)
- 確定: 670件 (Win 169 / Loss 211 / Flat 290) / skip 755件
- 成長率目線: 平均log +0.000383 / 幾何平均 +0.038% per trade / maxDD +4.72%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: POND/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $129.24

## 4. Latest Market Context

- 更新: 2026-05-25T17:24:19.311151+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.10% price=77617.7
- Funnel: target 765 → liquid 121 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| POND/USDT:USDT | +80.00% | $1,131,684.13 |
| TONCOIN/USDT:USDT | +9.58% | $42,778,283.22 |
| NIL/USDT:USDT | +8.48% | $17,677,288.87 |
| H/USDT:USDT | +5.18% | $2,097,869.65 |
| GRASS/USDT:USDT | +4.37% | $3,680,061.99 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NIL/USDT:USDT | below_1h_threshold | +4.48% | +4.58% |
| TONCOIN/USDT:USDT | below_1h_threshold | +3.90% | +4.00% |
| BSB/USDT:USDT | below_1h_threshold | +3.85% | +3.95% |
| LIT/USDT:USDT | below_1h_threshold | +2.95% | +3.04% |
| GRASS/USDT:USDT | below_1h_threshold | +2.29% | +2.39% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
