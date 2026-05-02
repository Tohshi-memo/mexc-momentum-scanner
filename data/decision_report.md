# Decision Report

- generated_at: 2026-05-02T15:32:20.710142+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2929**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2929, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=-3.12%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -3.12% | **-3.12%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 10/20 | 50.0% | +3.11% | **+1.55%** |
| LIMIT_8PCT | 4/20 | 20.0% | +6.93% | **+1.39%** |
| LIMIT_7PCT | 6/20 | 30.0% | +4.54% | **+1.36%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_5PCT | 14/20 | 70.0% | +0.75% | **+0.52%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +5.93% | **+5.93%** |
| MARKET_LONG | 20/20 | 100.0% | +1.54% | **+1.54%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.70% | **+1.44%** |
| LIMIT_5PCT_LONG | 6/20 | 30.0% | +4.14% | **+1.24%** |
| ASK_LONG | 20/20 | 100.0% | +1.18% | **+1.18%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 8件 (TP 4 / SL 4 / EXP 0)
- 最新: NAORIS/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-02T15:32:17.817684+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=78338.0
- Funnel: target 755 → liquid 161 → pre 50 → checked 50 → surge 4 → strict 0
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 89.2 >= 65=1, 4h RSI 96.2 >= 65=1, 4h RSI 82.0 >= 65=1, 4h RSI 75.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +318.84% | $165,763,172.30 |
| TAG/USDT:USDT | +71.02% | $10,040,719.38 |
| BIO/USDT:USDT | +46.24% | $3,910,984.19 |
| SKYAI/USDT:USDT | +35.60% | $19,142,809.28 |
| ORDI/USDT:USDT | +26.57% | $14,992,809.63 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TAG/USDT:USDT | below_1h_threshold | +4.38% | +4.44% |
| B/USDT:USDT | below_1h_threshold | +2.90% | +2.96% |
| NAORIS/USDT:USDT | below_1h_threshold | +2.43% | +2.48% |
| UB/USDT:USDT | below_1h_threshold | +2.36% | +2.42% |
| XNY/USDT:USDT | below_1h_threshold | +1.80% | +1.85% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
