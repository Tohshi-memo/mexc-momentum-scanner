# Decision Report

- generated_at: 2026-05-02T21:32:35.224537+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2985**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2985, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=-0.95%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.95% | **-0.95%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_BB3S | 5/16 | 31.2% | +1.45% | **+0.45%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.33% | **+0.13%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.95% | **+1.17%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +2.13% | **+1.17%** |
| MARKET_LONG | 20/20 | 100.0% | +1.00% | **+1.00%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +6.07% | **+0.91%** |
| ASK_LONG | 20/20 | 100.0% | +0.74% | **+0.74%** |

## 2. $100 Live Portfolio

- 残高: **$102.70** / 初期 $100.00 (+2.70%)
- 確定トレード: 9件 (TP 4 / SL 4 / EXP 1)
- 最新: RAVE/USDT:USDT EXPIRED PnL +5.55% 残高後 $102.70
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-02T21:32:32.601954+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.10% price=78496.0
- Funnel: target 755 → liquid 165 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.8 >= 65=1, 4h RSI 70.1 >= 65=1, 4h RSI 84.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +28.27% | $299,084,455.26 |
| XNY/USDT:USDT | +18.06% | $2,030,392.75 |
| NAORIS/USDT:USDT | +14.37% | $4,367,078.48 |
| CHILLGUY/USDT:USDT | +12.73% | $1,164,309.36 |
| LUNC/USDT:USDT | +11.87% | $28,304,474.62 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKYAI/USDT:USDT | below_1h_threshold | +4.88% | +4.78% |
| NAORIS/USDT:USDT | below_1h_threshold | +2.95% | +2.84% |
| SPACE/USDT:USDT | below_1h_threshold | +2.79% | +2.69% |
| TRB/USDT:USDT | below_1h_threshold | +2.74% | +2.64% |
| CHILLGUY/USDT:USDT | below_1h_threshold | +2.66% | +2.56% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
