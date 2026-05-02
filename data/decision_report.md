# Decision Report

- generated_at: 2026-05-02T12:21:56.255571+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2900**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2900, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +4.33% | **+1.08%** |
| LIMIT_5PCT | 12/20 | 60.0% | +1.54% | **+0.92%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.32% | **+0.24%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +0.07% | **+0.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +4.40% | **+3.08%** |
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +3.23% | **+2.42%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +3.12% | **+2.34%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.36% | **+1.22%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +2.67% | **+1.20%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 8件 (TP 4 / SL 4 / EXP 0)
- 最新: NAORIS/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-02T12:21:54.313821+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=78100.0
- Funnel: target 755 → liquid 168 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +219.16% | $125,135,303.68 |
| TAG/USDT:USDT | +30.48% | $5,066,502.35 |
| BIO/USDT:USDT | +28.42% | $2,131,256.70 |
| TAC/USDT:USDT | +25.71% | $1,942,626.71 |
| SPACE/USDT:USDT | +21.36% | $1,217,544.06 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +3.95% | +3.96% |
| SKYAI/USDT:USDT | below_1h_threshold | +3.93% | +3.94% |
| ORCA/USDT:USDT | below_1h_threshold | +3.58% | +3.59% |
| USTC/USDT:USDT | below_1h_threshold | +3.54% | +3.55% |
| BIO/USDT:USDT | below_1h_threshold | +2.79% | +2.79% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
