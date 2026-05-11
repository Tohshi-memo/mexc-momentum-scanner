# Decision Report

- generated_at: 2026-05-11T20:22:56.794218+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4067**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4067, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=-1.07%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.07% | **-1.07%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_6PCT | 6/20 | 30.0% | +0.94% | **+0.28%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.05% | **+1.75%** |
| ASK_LONG | 20/20 | 100.0% | +1.37% | **+1.37%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +2.08% | **+1.35%** |
| MARKET_LONG | 20/20 | 100.0% | +1.23% | **+1.23%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +1.40% | **+0.70%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 33件 (TP 8 / SL 22 / EXP 3)
- 最新: SIREN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$107.86** / 初期 $100.00 (+7.86%)
- 確定: 218件 (Win 54 / Loss 76 / Flat 88) / skip 410件
- 成長率目線: 平均log +0.000347 / 幾何平均 +0.035% per trade / maxDD +4.09%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: B/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $107.86

## 4. Latest Market Context

- 更新: 2026-05-11T20:22:53.734863+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.11% price=81829.9
- Funnel: target 757 → liquid 192 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| USELESS/USDT:USDT | +15.00% | $2,593,073.58 |
| SKYAI/USDT:USDT | +14.80% | $34,714,796.71 |
| B/USDT:USDT | +13.95% | $34,271,077.82 |
| SAGA/USDT:USDT | +13.85% | $5,834,763.34 |
| GIGA/USDT:USDT | +11.43% | $1,245,223.59 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ASTSSTOCK/USDT:USDT | below_1h_threshold | +4.42% | +4.53% |
| ASTEROID/USDT:USDT | below_1h_threshold | +3.09% | +3.20% |
| LAB/USDT:USDT | below_1h_threshold | +1.64% | +1.74% |
| LUNC/USDT:USDT | below_1h_threshold | +1.57% | +1.68% |
| NIL/USDT:USDT | below_1h_threshold | +1.50% | +1.61% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
