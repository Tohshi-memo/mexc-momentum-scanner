# Decision Report

- generated_at: 2026-05-01T23:22:06.891723+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2842**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2842, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+0.04%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.04% | **+0.04%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 20/20 | 100.0% | +0.85% | **+0.85%** |
| LIMIT_2PCT | 18/20 | 90.0% | +0.70% | **+0.63%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +1.36% | **+0.61%** |
| ASK | 20/20 | 100.0% | +0.61% | **+0.61%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +2.20% | **+1.10%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +2.77% | **+0.97%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.49% | **+0.97%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.41% | **+0.77%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.48% | **+0.34%** |

## 2. $100 Live Portfolio

- 残高: **$103.02** / 初期 $100.00 (+3.02%)
- 確定トレード: 6件 (TP 4 / SL 2 / EXP 0)
- 最新: RLS/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.02
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-01T23:22:04.983056+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=78045.8
- Funnel: target 755 → liquid 185 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 81.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +55.04% | $13,112,457.95 |
| WOJAK/USDT:USDT | +13.41% | $1,066,465.83 |
| CHILLGUY/USDT:USDT | +12.59% | $1,068,148.10 |
| BLESS/USDT:USDT | +10.66% | $1,165,658.84 |
| RLS/USDT:USDT | +9.45% | $2,580,078.60 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FIGHT/USDT:USDT | below_1h_threshold | +2.45% | +2.53% |
| WOJAK/USDT:USDT | below_1h_threshold | +2.27% | +2.35% |
| AIGENSYN/USDT:USDT | below_1h_threshold | +1.83% | +1.91% |
| VELVET/USDT:USDT | below_1h_threshold | +1.57% | +1.65% |
| MEGA/USDT:USDT | below_1h_threshold | +1.33% | +1.41% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
