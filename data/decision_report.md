# Decision Report

- generated_at: 2026-05-04T01:02:29.947683+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3120**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3120, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=-0.74%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.74% | **-0.74%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_BB3S | 6/19 | 31.6% | +0.20% | **+0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +4.80% | **+1.92%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.84% | **+1.20%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.50% | **+1.13%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.74% | **+1.04%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.45% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$103.21** / 初期 $100.00 (+3.21%)
- 確定トレード: 11件 (TP 5 / SL 5 / EXP 1)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T01:02:25.720112+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.12% price=78413.0
- Funnel: target 756 → liquid 160 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +64.67% | $241,615,676.43 |
| SKYAI/USDT:USDT | +55.74% | $30,580,889.90 |
| GIGA/USDT:USDT | +24.52% | $1,078,178.40 |
| BSB/USDT:USDT | +22.22% | $15,014,141.86 |
| TAG/USDT:USDT | +19.24% | $3,715,445.76 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKYAI/USDT:USDT | below_1h_threshold | +1.64% | +1.75% |
| TRADOOR/USDT:USDT | below_1h_threshold | +1.58% | +1.70% |
| BR/USDT:USDT | below_1h_threshold | +1.18% | +1.29% |
| BSB/USDT:USDT | below_1h_threshold | +0.92% | +1.04% |
| TAG/USDT:USDT | below_1h_threshold | +0.90% | +1.02% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
