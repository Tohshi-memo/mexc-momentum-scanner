# Decision Report

- generated_at: 2026-06-04T01:59:06.330685+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5590**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.91% / filled 20/20。**
- 全期間 MARKET基準: n=5590, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=+2.91%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.91% | **+2.91%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +2.93% | **+2.93%** |
| MARKET | 20/20 | 100.0% | +2.91% | **+2.91%** |
| LIMIT_1PCT | 17/20 | 85.0% | +2.68% | **+2.28%** |
| LIMIT_2PCT | 13/20 | 65.0% | +2.32% | **+1.51%** |
| LIMIT_ATR | 12/20 | 60.0% | +2.49% | **+1.49%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +2.48% | **+0.62%** |
| LIMIT_BB3S_LONG | 2/5 | 40.0% | +0.69% | **+0.27%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +0.28% | **+0.17%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | -0.58% | **-0.29%** |

## 2. $100 Live Portfolio

- 残高: **$99.04** / 初期 $100.00 (-0.96%)
- 確定トレード: 94件 (TP 29 / SL 62 / EXP 3)
- 最新: ICP/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.04
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.20** / 初期 $100.00 (+31.20%)
- 確定: 1005件 (Win 239 / Loss 312 / Flat 454) / skip 1146件
- 成長率目線: 平均log +0.000270 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LIT/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $131.20

## 4. Latest Market Context

- 更新: 2026-06-04T01:59:03.940122+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -1.83% price=62151.8
- Funnel: target 771 → liquid 148 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| OPN/USDT:USDT | +24.55% | $22,967,314.56 |
| STO/USDT:USDT | +16.53% | $6,808,236.64 |
| MAGMA/USDT:USDT | +8.57% | $4,372,869.95 |
| EPIC/USDT:USDT | +7.95% | $3,572,079.35 |
| ZORA/USDT:USDT | +7.04% | $1,220,087.03 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZORA/USDT:USDT | below_1h_threshold | +4.52% | +6.35% |
| MAGMA/USDT:USDT | below_1h_threshold | +1.32% | +3.15% |
| EPIC/USDT:USDT | below_1h_threshold | +1.06% | +2.89% |
| LAB/USDT:USDT | below_1h_threshold | +1.01% | +2.85% |
| XAU/USDT:USDT | below_1h_threshold | +0.37% | +2.20% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
