# Decision Report

- generated_at: 2026-05-02T03:32:11.644419+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2856**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2856, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=-0.82%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.82% | **-0.82%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +4.33% | **+1.08%** |
| LIMIT_8PCT | 3/20 | 15.0% | +6.57% | **+0.99%** |
| LIMIT_7PCT | 3/20 | 15.0% | +6.27% | **+0.94%** |
| LIMIT_5PCT | 5/20 | 25.0% | +2.36% | **+0.59%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +2.00% | **+0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +2.42% | **+1.45%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.60% | **+1.04%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.68% | **+1.01%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +2.00% | **+1.00%** |
| LIMIT_6PCT_LONG | 6/20 | 30.0% | +2.62% | **+0.79%** |

## 2. $100 Live Portfolio

- 残高: **$102.51** / 初期 $100.00 (+2.51%)
- 確定トレード: 7件 (TP 4 / SL 3 / EXP 0)
- 最新: BIO/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.51
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-02T03:32:09.622992+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=78338.2
- Funnel: target 755 → liquid 173 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +94.21% | $32,573,477.41 |
| SKYAI/USDT:USDT | +17.80% | $21,722,834.91 |
| B/USDT:USDT | +14.35% | $70,213,706.17 |
| BLESS/USDT:USDT | +12.76% | $1,758,752.71 |
| PLAY/USDT:USDT | +10.39% | $4,453,842.37 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TAC/USDT:USDT | below_1h_threshold | +4.43% | +4.41% |
| UB/USDT:USDT | below_1h_threshold | +3.13% | +3.10% |
| BSB/USDT:USDT | below_1h_threshold | +2.61% | +2.59% |
| VELVET/USDT:USDT | below_1h_threshold | +2.49% | +2.46% |
| CHIP/USDT:USDT | below_1h_threshold | +2.43% | +2.40% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
