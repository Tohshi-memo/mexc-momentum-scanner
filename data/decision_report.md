# Decision Report

- generated_at: 2026-05-01T12:57:05.668728+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2798**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2798, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=-0.67%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.67% | **-0.67%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 9/20 | 45.0% | +1.94% | **+0.87%** |
| LIMIT_7PCT | 7/20 | 35.0% | +2.34% | **+0.82%** |
| LIMIT_9PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_8PCT | 5/20 | 25.0% | +1.48% | **+0.37%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +2.29% | **+2.18%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.12% | **+1.59%** |
| MARKET_LONG | 20/20 | 100.0% | +1.27% | **+1.27%** |
| ASK_LONG | 20/20 | 100.0% | +0.91% | **+0.91%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.30% | **+0.78%** |

## 2. $100 Live Portfolio

- 残高: **$102.51** / 初期 $100.00 (+2.51%)
- 確定トレード: 4件 (TP 3 / SL 1 / EXP 0)
- 最新: PLAY/USDT:USDT TP_HIT PnL +7.74% 残高後 $102.51
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-01T12:57:01.348225+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.66% price=77939.3
- Funnel: target 760 → liquid 201 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 81.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B/USDT:USDT | +62.08% | $14,074,085.69 |
| UB/USDT:USDT | +61.37% | $20,156,010.87 |
| NFP/USDT:USDT | +38.05% | $1,429,960.61 |
| BR/USDT:USDT | +37.41% | $25,668,528.07 |
| ORCA/USDT:USDT | +33.71% | $11,305,261.45 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ST/USDT:USDT | below_1h_threshold | +4.25% | +3.59% |
| APE/USDT:USDT | below_1h_threshold | +2.55% | +1.89% |
| ORCA/USDT:USDT | below_1h_threshold | +2.43% | +1.77% |
| RAY/USDT:USDT | below_1h_threshold | +1.76% | +1.10% |
| INJ/USDT:USDT | below_1h_threshold | +1.49% | +0.83% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
