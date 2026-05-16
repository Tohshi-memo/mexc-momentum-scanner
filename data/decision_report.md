# Decision Report

- generated_at: 2026-05-16T01:48:42.424247+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4363**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4363, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+0.09%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.09% | **+0.09%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 7/20 | 35.0% | +1.25% | **+0.44%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.94% | **+0.39%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.37% | **+0.22%** |
| ASK | 20/20 | 100.0% | +0.14% | **+0.14%** |
| MARKET | 20/20 | 100.0% | +0.09% | **+0.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +1.17% | **+0.58%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +1.33% | **+0.40%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.91% | **+0.36%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.09% | **+0.08%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | -0.17% | **-0.10%** |

## 2. $100 Live Portfolio

- 残高: **$97.20** / 初期 $100.00 (-2.80%)
- 確定トレード: 47件 (TP 12 / SL 32 / EXP 3)
- 最新: NAORIS/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.20
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$117.99** / 初期 $100.00 (+17.99%)
- 確定: 391件 (Win 97 / Loss 136 / Flat 158) / skip 533件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +4.21%
- 次の候補: `LIMIT_6PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: STORJ/USDT:USDT `LIMIT_6PCT_LONG` EXPIRED account +0.00% 残高後 $117.99

## 4. Latest Market Context

- 更新: 2026-05-16T01:48:36.074311+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=79030.2
- Funnel: target 759 → liquid 168 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| STORJ/USDT:USDT | +26.61% | $5,694,253.18 |
| ARCSOL/USDT:USDT | +25.99% | $1,329,652.15 |
| ASTEROID/USDT:USDT | +23.36% | $3,506,487.82 |
| LAB/USDT:USDT | +20.13% | $154,168,326.39 |
| PEAQ/USDT:USDT | +12.34% | $4,327,009.62 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SAHARA/USDT:USDT | below_1h_threshold | +3.13% | +3.19% |
| UP/USDT:USDT | below_1h_threshold | +3.09% | +3.15% |
| GUA/USDT:USDT | below_1h_threshold | +2.97% | +3.02% |
| PLAY/USDT:USDT | below_1h_threshold | +2.36% | +2.41% |
| ESPORTS/USDT:USDT | below_1h_threshold | +2.31% | +2.37% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
