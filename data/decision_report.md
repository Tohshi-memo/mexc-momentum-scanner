# Decision Report

- generated_at: 2026-05-02T16:52:17.529251+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2960**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2960, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=+0.13%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.13% | **+0.13%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +0.62% | **+0.59%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +2.00% | **+0.60%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.01% | **+0.45%** |
| MARKET_LONG | 20/20 | 100.0% | +0.44% | **+0.44%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.47% | **+0.35%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.67% | **+0.27%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 8件 (TP 4 / SL 4 / EXP 0)
- 最新: NAORIS/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-02T16:52:09.943920+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=78454.8
- Funnel: target 755 → liquid 165 → pre 50 → checked 50 → surge 7 → strict 2
- Surge前reject: below_1h_threshold=43, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.8 >= 65=1, 4h RSI 96.9 >= 65=1, 4h RSI 79.6 >= 65=1, 4h RSI 65.1 >= 65=1, 4h RSI 85.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TAG/USDT:USDT | +30.54% | $13,256,706.71 |
| LAB/USDT:USDT | +17.62% | $196,618,116.55 |
| TAC/USDT:USDT | +8.72% | $2,506,683.34 |
| XNY/USDT:USDT | +6.17% | $1,250,095.48 |
| BIANRENSHENG/USDT:USDT | +5.87% | $1,002,180.06 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ALCH/USDT:USDT | below_1h_threshold | +4.37% | +4.36% |
| PNUT/USDT:USDT | below_1h_threshold | +4.09% | +4.08% |
| PLAY/USDT:USDT | below_1h_threshold | +3.44% | +3.43% |
| NAORIS/USDT:USDT | below_1h_threshold | +3.13% | +3.12% |
| CHILLGUY/USDT:USDT | below_1h_threshold | +3.06% | +3.06% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
