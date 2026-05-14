# Decision Report

- generated_at: 2026-05-14T03:13:01.605777+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4268**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.99% / filled 20/20。**
- 全期間 MARKET基準: n=4268, expectancy=-0.11%
- 直近20件 MARKET基準: n=20, expectancy=+0.99%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.99% | **+0.99%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.01% | **+1.01%** |
| MARKET | 20/20 | 100.0% | +0.99% | **+0.99%** |
| LIMIT_3PCT | 13/20 | 65.0% | +1.48% | **+0.96%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.96% | **+0.81%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.53% | **+0.37%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/5 | 40.0% | +2.90% | **+1.16%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.69% | **+0.67%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.71% | **+0.57%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +0.72% | **+0.43%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +1.33% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$97.21** / 初期 $100.00 (-2.79%)
- 確定トレード: 41件 (TP 10 / SL 28 / EXP 3)
- 最新: SAGA/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.21
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$119.18** / 初期 $100.00 (+19.18%)
- 確定: 343件 (Win 94 / Loss 125 / Flat 124) / skip 486件
- 成長率目線: 平均log +0.000512 / 幾何平均 +0.051% per trade / maxDD +4.21%
- 次の候補: `LIMIT_7PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: IRYS/USDT:USDT `LIMIT_7PCT_LONG` EXPIRED account +0.00% 残高後 $119.18

## 4. Latest Market Context

- 更新: 2026-05-14T03:12:58.364810+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.14% price=79218.4
- Funnel: target 765 → liquid 169 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SAGA/USDT:USDT | +31.49% | $15,372,630.97 |
| IRYS/USDT:USDT | +24.76% | $6,171,334.51 |
| TROLLSOL/USDT:USDT | +22.70% | $1,931,358.90 |
| UP/USDT:USDT | +22.19% | $5,024,325.56 |
| CSCOSTOCK/USDT:USDT | +21.27% | $4,818,774.54 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GIGA/USDT:USDT | below_1h_threshold | +2.56% | +2.70% |
| SAGA/USDT:USDT | below_1h_threshold | +2.36% | +2.49% |
| UP/USDT:USDT | below_1h_threshold | +1.83% | +1.97% |
| LAB/USDT:USDT | below_1h_threshold | +1.70% | +1.84% |
| AIGENSYN/USDT:USDT | below_1h_threshold | +1.01% | +1.15% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
