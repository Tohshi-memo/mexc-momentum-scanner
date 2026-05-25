# Decision Report

- generated_at: 2026-05-25T17:14:14.072175+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4863**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4863, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-2.19%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.19% | **-2.19%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 5/20 | 25.0% | +1.01% | **+0.25%** |
| LIMIT_7PCT | 4/20 | 20.0% | +0.87% | **+0.17%** |
| LIMIT_8PCT | 3/20 | 15.0% | +0.09% | **+0.01%** |
| LIMIT_10PCT | 3/20 | 15.0% | +0.09% | **+0.01%** |
| LIMIT_9PCT | 3/20 | 15.0% | +0.09% | **+0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/7 | 71.4% | +4.40% | **+3.15%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +4.35% | **+2.83%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +4.15% | **+2.07%** |
| ASK_LONG | 20/20 | 100.0% | +1.87% | **+1.87%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +3.33% | **+1.83%** |

## 2. $100 Live Portfolio

- 残高: **$96.68** / 初期 $100.00 (-3.32%)
- 確定トレード: 63件 (TP 17 / SL 43 / EXP 3)
- 最新: KITE/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.68
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$129.89** / 初期 $100.00 (+29.89%)
- 確定: 669件 (Win 169 / Loss 210 / Flat 290) / skip 755件
- 成長率目線: 平均log +0.000391 / 幾何平均 +0.039% per trade / maxDD +4.72%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $129.89

## 4. Latest Market Context

- 更新: 2026-05-25T17:14:09.490610+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=77660.3
- Funnel: target 765 → liquid 121 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| POND/USDT:USDT | +86.42% | $1,096,555.87 |
| TONCOIN/USDT:USDT | +9.10% | $40,075,507.02 |
| TIA/USDT:USDT | +5.54% | $9,628,256.80 |
| NIL/USDT:USDT | +5.20% | $17,530,607.62 |
| H/USDT:USDT | +5.18% | $2,077,615.83 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| POND/USDT:USDT | below_1h_threshold | +4.40% | +4.44% |
| LIT/USDT:USDT | below_1h_threshold | +3.76% | +3.80% |
| TONCOIN/USDT:USDT | below_1h_threshold | +3.45% | +3.50% |
| AGT/USDT:USDT | below_1h_threshold | +2.04% | +2.09% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +1.69% | +1.74% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
