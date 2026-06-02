# Decision Report

- generated_at: 2026-06-02T08:04:35.991866+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5423**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5423, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 11/19 | 57.9% | +0.96% | **+0.56%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +3.08% | **+0.46%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.59% | **+0.46%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +2.16% | **+1.73%** |
| MARKET_LONG | 20/20 | 100.0% | +1.20% | **+1.20%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.35% | **+0.88%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.96% | **+0.82%** |
| ASK_LONG | 20/20 | 100.0% | +0.81% | **+0.81%** |

## 2. $100 Live Portfolio

- 残高: **$96.63** / 初期 $100.00 (-3.37%)
- 確定トレード: 84件 (TP 24 / SL 57 / EXP 3)
- 最新: PORTAL/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.63
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$134.45** / 初期 $100.00 (+34.45%)
- 確定: 935件 (Win 220 / Loss 280 / Flat 435) / skip 1049件
- 成長率目線: 平均log +0.000317 / 幾何平均 +0.032% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: H/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $134.45

## 4. Latest Market Context

- 更新: 2026-06-02T08:04:33.323564+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.13% price=69990.7
- Funnel: target 772 → liquid 150 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| US/USDT:USDT | +45.19% | $1,767,722.11 |
| SKYAI/USDT:USDT | +34.32% | $15,843,808.82 |
| ESPORTS/USDT:USDT | +30.71% | $12,178,684.57 |
| LAB/USDT:USDT | +21.87% | $215,602,563.40 |
| MRVLSTOCK/USDT:USDT | +20.91% | $2,755,061.22 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ESPORTS/USDT:USDT | below_1h_threshold | +4.37% | +4.50% |
| MERL/USDT:USDT | below_1h_threshold | +1.08% | +1.21% |
| EPIC/USDT:USDT | below_1h_threshold | +0.96% | +1.09% |
| BSB/USDT:USDT | below_1h_threshold | +0.91% | +1.04% |
| MYX/USDT:USDT | below_1h_threshold | +0.84% | +0.97% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
