# Decision Report

- generated_at: 2026-05-02T15:22:08.252065+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2927**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2927, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-3.12%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -3.12% | **-3.12%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 4/20 | 20.0% | +6.93% | **+1.39%** |
| LIMIT_6PCT | 9/20 | 45.0% | +2.57% | **+1.15%** |
| LIMIT_7PCT | 5/20 | 25.0% | +3.84% | **+0.96%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_5PCT | 13/20 | 65.0% | +0.19% | **+0.12%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.94% | **+1.94%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.23% | **+1.89%** |
| ASK_LONG | 20/20 | 100.0% | +1.57% | **+1.57%** |
| LIMIT_6PCT_LONG | 5/20 | 25.0% | +5.97% | **+1.49%** |
| LIMIT_5PCT_LONG | 5/20 | 25.0% | +5.77% | **+1.44%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 8件 (TP 4 / SL 4 / EXP 0)
- 最新: NAORIS/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-02T15:22:06.095138+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=78331.6
- Funnel: target 755 → liquid 160 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +287.10% | $161,400,156.56 |
| TAG/USDT:USDT | +73.04% | $9,813,289.73 |
| BIO/USDT:USDT | +50.10% | $3,820,359.93 |
| SKYAI/USDT:USDT | +34.36% | $18,763,334.88 |
| BSB/USDT:USDT | +26.39% | $7,475,112.06 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKYAI/USDT:USDT | below_1h_threshold | +4.58% | +4.64% |
| ORDI/USDT:USDT | below_1h_threshold | +4.49% | +4.55% |
| BSB/USDT:USDT | below_1h_threshold | +3.34% | +3.41% |
| NAORIS/USDT:USDT | below_1h_threshold | +2.24% | +2.30% |
| B/USDT:USDT | below_1h_threshold | +1.78% | +1.84% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
